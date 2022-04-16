import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from models.register import RegisterUserModel

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

    def entry_data_login(self, data: RegisterUserModel):
        logger.info(f"Login user with email={data.user} and password {data.password_1}")
        self.fill(locator=self.EMAIL_FIELD, value=data.user)
        self.fill(locator=self.PASSWORD_FIELD, value=data.password_1)
        self.click(locator=self.LOGIN_BUTTON)

    def get_event_text(self) -> str:
        self.click(locator=self.LOGIN_BUTTON)
        success = self.text(locator=self.SUCCESS_TEXT)
        return success
