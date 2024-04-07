import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions


class Config:
    ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DOWNLOADS_PATH = os.path.abspath(os.path.join(ROOT_PATH, 'data/downloads/'))

    def __init__(self) -> None:
        with open(os.path.join(self.ROOT_PATH, 'config.json')) as file:
            personal_config = json.load(file)
            self.base_url = personal_config['url']
            self.browser = personal_config['BROWSER']
            self.browser_mode = personal_config['BROWSER_MODE']
            self.base_timeout = personal_config['base_timeout']
            self.driver_path = personal_config["driver_path"]

    def get_web_driver(self, mobile=False):
        drv_path = os.path.join(self.ROOT_PATH, self.driver_path)
        options = ChromeOptions()
        if mobile:
            mobile_emulation = {
                "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
                "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) "
                             "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
            }
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            options.add_experimental_option("prefs", {
                "download.default_directory": self.DOWNLOADS_PATH,
                "profile.default_content_setting_values.automatic_downloads": 1
            })
        else:
            options.add_experimental_option("prefs", {
                "download.default_directory": self.DOWNLOADS_PATH,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": False,
                'safebrowsing.disable_download_protection': True,
                "profile.default_content_setting_values.automatic_downloads": 1,
                "profile.default_content_setting_values.media_stream_camera": 1,
            })
        service = Service(executable_path=drv_path)
        if self.browser == 'chrome' and (self.browser_mode == 'display' or not self.browser_mode):
            driver = webdriver.Chrome(service=service, options=options)
        elif self.browser == 'chrome' and self.browser_mode == 'headless':
            options = ChromeOptions()
            options.headless = True
            options.add_argument('disable-gpu')
            options.add_argument('window-size=1920,1080')
            driver = webdriver.Chrome(options=options, service=service)
            params = {'behavior': 'allow', 'downloadPath': self.DOWNLOADS_PATH}
            driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
        elif self.browser == 'ie':
            driver = webdriver.Ie(drv_path)
        elif self.browser == 'edge':
            driver = webdriver.Edge(drv_path)
        driver.maximize_window()
        return driver
