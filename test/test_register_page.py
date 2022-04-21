from fixtures.constants import Notice
from models.register import RegisterUserModel


class TestRegisterPage:

    def test_valid_registration(self, app):
        """
        Успешная регистрация.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        app.register_page.register_user(data=data)
        assert app.register_page.get_success_text() == Notice.SUCCESSFUL_ACTION

    def test_invalid_email_registration(self, app):
        """
        Регистрация с невалидным email.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.user = data.domain
        app.register_page.register_user(data=data)
        assert app.register_page.get_error_text() == f"Error, {data.user} is not email address!"

    def test_invalid_password_registration(self, app):
        """
        Регистрация с разными паролями.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_2 = None
        app.register_page.register_user(data=data)
        assert app.register_page.get_error_text() == Notice.ERROR_DIFFERENT_PASS

    def test_short_password_registration(self, app):
        """
        Регистрация с паролем < 7 симвлов.
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_1 = "1234"
        data.password_2 = "1234"
        app.register_page.register_user(data=data)
        assert app.register_page.get_error_text() == Notice.ERROR_PASS_TOO_SHORT
