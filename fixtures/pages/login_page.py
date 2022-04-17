import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("react_shop")


class LoginPage(BasePage):
    CHAPTER_LOGIN = (By.ID, "login-link")
    EMAIL_FIELD = (By.ID, "name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "register")
    SUCCESS_TEXT = (By.CLASS_NAME, "toast")

    def open_login_page(self):
        logger.info("")
        self.open_page(self.app.url)
        self.click(locator=self.CHAPTER_LOGIN)

    def entry_data_login(self, user: str, password: str):
        logger.info(f"Login user with email={user} and password {password}")
        self.fill(locator=self.EMAIL_FIELD, value=user)
        self.fill(locator=self.PASSWORD_FIELD, value=password)
        self.click(locator=self.LOGIN_BUTTON)

    def get_event_text(self) -> str:
        self.click(locator=self.LOGIN_BUTTON)
        success = self.text(locator=self.SUCCESS_TEXT)
        return success
