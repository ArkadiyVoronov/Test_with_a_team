from selenium.webdriver.common.by import By

from models.register import RegisterUserModel, InvalidEmailRegisterUserModel, InvalidPasswordRegisterUserModel, \
    ShortPasswordRegisterUserModel


class RegisterPage:
    CHAPTER_REGISTER = (By.ID, "register-link")
    EMAIL_FIELD = (By.ID, "name")
    PASSWORD_FIELD = (By.ID, "password1")
    REPEAT_PASSWORD_FIELD = (By.ID, "password2")
    REGISTER_BUTTON = (By.ID, "register")
    ERROR_TEXT = (By.CLASS_NAME, "card-panel")

    def __init__(self, app):
        self.app = app

    def open_register_page(self):
        self.app.driver.get(self.app.url)
        chapter_register = self.app.driver.find_element(*self.CHAPTER_REGISTER)
        chapter_register.click()

    def register_user(self, data: RegisterUserModel):
        self._fill_in_email(data.user)
        self._fill_in_password1(data.password_1)
        self._fill_in_password2(data.password_2)
        self._register_button_click()

    def invalid_email_register_user(self, data: InvalidEmailRegisterUserModel):
        self._fill_in_email(data.user)
        self._fill_in_password1(data.password_1)
        self._fill_in_password2(data.password_2)
        self._register_button_click()

    def invalid_password_register_user(self, data: InvalidPasswordRegisterUserModel):
        self._fill_in_email(data.user)
        self._fill_in_password1(data.password_1)
        self._fill_in_password2(data.password_2)
        self._register_button_click()

    def short_password_register_user(self, data: ShortPasswordRegisterUserModel):
        self._fill_in_email(data.user)
        self._fill_in_password1(data.password_1)
        self._fill_in_password2(data.password_2)
        self._register_button_click()

    def _register_button_click(self):
        register_button = self.app.driver.find_element(*self.REGISTER_BUTTON)
        register_button.click()

    def _fill_in_email(self, value: str):
        email_field = self.app.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(value)

    def _fill_in_password1(self, value: str):
        email_field = self.app.driver.find_element(*self.PASSWORD_FIELD)
        email_field.send_keys(value)

    def _fill_in_password2(self, value: str):
        email_field = self.app.driver.find_element(*self.REPEAT_PASSWORD_FIELD)
        email_field.send_keys(value)

    def get_error_text(self) -> str:
        #заменить его на register user
        register_button = self.app.driver.find_element(*self.REGISTER_BUTTON)
        register_button.click()
        error = self.app.driver.find_element(*self.ERROR_TEXT)
        return error.text