from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from models.register import RegisterUserModel, InvalidEmailRegisterUserModel,\
    InvalidPasswordRegisterUserModel, ShortPasswordRegisterUserModel


class RegisterPage(BasePage):
    CHAPTER_REGISTER = (By.ID, "register-link")
    EMAIL_FIELD = (By.ID, "name")
    PASSWORD_FIELD = (By.ID, "password1")
    REPEAT_PASSWORD_FIELD = (By.ID, "password2")
    REGISTER_BUTTON = (By.ID, "register")
    ERROR_TEXT = (By.CLASS_NAME, "card-panel")
    SUCCESS_TEXT = (By.CLASS_NAME, "toast")

    def open_register_page(self):
        self.open_page(self.app.url)
        self.click(locator=self.CHAPTER_REGISTER)

    def register_user(self, data: RegisterUserModel):
        self.fill(locator=self.EMAIL_FIELD, value=data.user)
        self.fill(locator=self.PASSWORD_FIELD, value=data.password_1)
        self.fill(locator=self.REPEAT_PASSWORD_FIELD, value=data.password_2)
        self.click(locator=self.REGISTER_BUTTON)

    def invalid_email_register_user(self, data: InvalidEmailRegisterUserModel):
        self.fill(locator=self.EMAIL_FIELD, value=data.user)
        self.fill(locator=self.PASSWORD_FIELD, value=data.password_1)
        self.fill(locator=self.REPEAT_PASSWORD_FIELD, value=data.password_2)
        self.click(locator=self.REGISTER_BUTTON)

    def invalid_password_register_user(self, data: InvalidPasswordRegisterUserModel):
        self.fill(locator=self.EMAIL_FIELD, value=data.user)
        self.fill(locator=self.PASSWORD_FIELD, value=data.password_1)
        self.fill(locator=self.REPEAT_PASSWORD_FIELD, value=data.password_2)
        self.click(locator=self.REGISTER_BUTTON)

    def short_password_register_user(self, data: ShortPasswordRegisterUserModel):
        self.fill(locator=self.EMAIL_FIELD, value=data.user)
        self.fill(locator=self.PASSWORD_FIELD, value=data.password_1)
        self.fill(locator=self.REPEAT_PASSWORD_FIELD, value=data.password_2)
        self.click(locator=self.REGISTER_BUTTON)

    def get_error_text(self) -> str:
        self.click(locator=self.REGISTER_BUTTON)
        error = self.text(locator=self.ERROR_TEXT)
        return error

    def get_success_text(self) -> str:
        self.click(locator=self.REGISTER_BUTTON)
        success = self.text(locator=self.SUCCESS_TEXT)
        return success
