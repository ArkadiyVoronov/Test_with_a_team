import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("react_shop")


class MainPage(BasePage):
    MAIN_LINK = (By.CLASS_NAME, "brand-logo")
    PRODUCT_TITLE = (By.XPATH, "//span[@class='card-title']")
    BUTTON_BUY_IN_MAIN = (By.XPATH, "//button[@class='btn']")
    SUCCESS_TEXT = (By.CLASS_NAME, "toast")
    BUTTON_BUY_IN_BASKET = (By.XPATH, "//button[@data-test='buy-btn']")
    BUTTON_BASKET = (By.CLASS_NAME, "material-icons")
    BUTTON_INCREASE_PRODUCT_IN_BASKET = (By.XPATH, "//i[@data-test='plus']")

    def open_main_page(self):
        self.open_page(self.app.url)

    def refresh_main(self):
        self.refresh_page(locator=self.MAIN_LINK)

    def load_store(self):
        self.click(locator=self.MAIN_LINK)

    def find_product(self):
        product = self.text(locator=self.PRODUCT_TITLE)
        return product

    def add_product_to_basket(self):
        logger.info("Add product to basket")
        self.click(locator=self.BUTTON_BUY_IN_MAIN)

    def get_event_text(self) -> str:
        self.click(locator=self.BUTTON_BUY_IN_MAIN)
        success = self.text(locator=self.SUCCESS_TEXT)
        return success

    def open_basket(self):
        self.click(locator=self.BUTTON_BASKET)

    def increase_products(self):
        self.click(locator=self.BUTTON_INCREASE_PRODUCT_IN_BASKET)

    def buy_product(self):
        logger.info("Buy product from basket")
        self.click(locator=self.BUTTON_BUY_IN_BASKET)
