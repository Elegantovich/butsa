from pages.base_page import BasePage


class Locators:
    pass


class MainPage(BasePage):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.loc = Locators
        self.url = app.base_url
