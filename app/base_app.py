from entities.config import Config
from robot.base_robot import BaseRobot
from selenium.webdriver.remote.webdriver import WebDriver


class Base_App:
    def __init__(self):
        self.config = Config()
        self.wd = WebDriver(self.config.get_web_driver())
        self.wd.implicitly_wait(self.config.base_timeout)
        self.robot = BaseRobot(self)
