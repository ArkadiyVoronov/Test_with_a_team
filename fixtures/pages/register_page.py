from selenium.webdriver.common.by import By


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

    def fill_in_email(self, value: str):
        email_field = self.app.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(value)

    def fill_in_password1(self, value: str):
        email_field = self.app.driver.find_element(*self.PASSWORD_FIELD)
        email_field.send_keys(value)

    def fill_in_password2(self, value: str):
        email_field = self.app.driver.find_element(*self.REPEAT_PASSWORD_FIELD)
        email_field.send_keys(value)

    def get_error_text(self) -> str:
        register_button = self.app.driver.find_element(*self.REGISTER_BUTTON)
        register_button.click()
        error = self.app.driver.find_element(*self.ERROR_TEXT)
        return error.text