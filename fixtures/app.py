from fixtures.pages.login_page import LoginPage
from fixtures.pages.main_page import MainPage
from fixtures.pages.register_page import RegisterPage
from fixtures.pages.balance_page import BalancePage


class Application:

    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.main_page = MainPage(self)
        self.balance_page = BalancePage(self)
        self.login_page = LoginPage(self)
        self.register_page = RegisterPage(self)

    def quit(self):
        self.driver.quit()
