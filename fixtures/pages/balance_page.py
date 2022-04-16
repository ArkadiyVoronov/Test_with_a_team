import logging

from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from models.register import RegisterUserModel
from models.balance import BalanceUserModel

logger = logging.getLogger("react_shop")


class BalancePage(BasePage):
    BALANCE_LINK = (By.ID, "blance-link")
    USER_NAME = (By.ID, "name")
    CARD_NUMBER = (By.ID, "card")
    CARD_DATE = (By.ID, "data-card")
    CARD_MONEY = (By.ID, "data-money")
    LABEL_AGREE = (By.ID, "agree")
    BUTTON_TRANSFER = (By.CLASS_NAME, "waves-effect")
    SUCCESS_TEXT = (By.CLASS_NAME, "toast")
    ERROR_TEXT = (By.CLASS_NAME, "card-panel")

    def open_balance_page(self):
        self.open_page(self.app.url)
        self.click(locator=self.BALANCE_LINK)

    def valid_balance(self, data: BalanceUserModel):
        logger.info("Verification valid balance")
        self.fill(locator=self.USER_NAME, value=data.user)
        self.fill(locator=self.CARD_NUMBER, value=data.card_number)
        self.fill(locator=self.CARD_DATE, value=data.card_date)
        self.fill(locator=self.CARD_MONEY, value=data.card_total)
        self.click(locator=self.LABEL_AGREE)
        self.click(locator=self.BUTTON_TRANSFER)

    def invalid_balance_checkbox(self, data: BalanceUserModel):
        logger.info("Verification invalid balance")
        self.fill(locator=self.USER_NAME, value=data.user)
        self.fill(locator=self.CARD_NUMBER, value=data.card_number)
        self.fill(locator=self.CARD_DATE, value=data.card_date)
        self.fill(locator=self.CARD_MONEY, value=data.card_total)
        self.click(locator=self.BUTTON_TRANSFER)

    def get_success_text(self) -> str:
        self.click(locator=self.BUTTON_TRANSFER)
        success = self.text(locator=self.SUCCESS_TEXT)
        return success

    def get_error_text(self) -> str:
        self.click(locator=self.BUTTON_TRANSFER)
        error = self.text(locator=self.ERROR_TEXT)
        return error
