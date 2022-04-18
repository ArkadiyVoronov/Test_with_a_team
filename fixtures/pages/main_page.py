import logging

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from models.balance import BalanceUserModel

logger = logging.getLogger("react_shop")


class MainPage(BasePage):
    MAIN_LINK = (By.CLASS_NAME, "brand-logo")
    PREPERE_DATA = (By.XPATH, "/main[@class='container content']/div[3]/button")
    PRODUCT_TITLE = (By.XPATH, "//span[@class='card-title']")
    CLICK_BUY = (By.XPATH, "//button[@class='btn']")
    SUCCESS_TEXT = (By.CLASS_NAME, "toast")

    def open_main_page(self):
        self.open_page(self.app.url)

    def load_store(self):
        self.click(locator=self.MAIN_LINK)

    def find_product(self):
        product = self.text(locator=self.PRODUCT_TITLE)
        return product

    def add_product(self):
        self.click(locator=self.CLICK_BUY)

    def get_success_text(self) -> str:
        self.click(locator=self.CLICK_BUY)
        success = self.text(locator=self.SUCCESS_TEXT)
        return success
