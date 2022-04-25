import logging
import os

from fixtures.pages.login_page import LoginPage
from fixtures.pages.main_page import MainPage
from fixtures.pages.register_page import RegisterPage
from fixtures.pages.balance_page import BalancePage

logger = logging.getLogger()


class Application:

    def __init__(self, driver, report_dir, url: str):
        logger.setLevel("INFO")
        self.create_dir_for_report(report_dir)
        self.driver = driver
        self.url = url
        self.main_page = MainPage(self)
        self.balance_page = BalancePage(self)
        self.login_page = LoginPage(self)
        self.register_page = RegisterPage(self)

    def quit(self):
        self.driver.quit()

    def create_allure_report(self, dir_name):
        cmd = f"allure generate {dir_name} -o {dir_name}/latest --clean"
        code_exit = os.system(cmd)
        logger.info(f"create_allure_report result : {code_exit}")

    @staticmethod
    def create_dir_for_report(dir_name):
        code_exit = os.system(f"rm -rf {dir_name}")
        logger.info(f"Drop old allure files : {code_exit}")
        os.makedirs(f"{dir_name}")
        logger.info(f"Create dir {dir_name}")

