from fixtures.constants import Notice
from models.register import RegisterUserModel, InvalidEmailRegisterUserModel,\
    InvalidPasswordRegisterUserModel, ShortPasswordRegisterUserModel


class TestRegisterPage:

    def test_valid_registration(self, app):
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        app.register_page.register_user(data=data)
        assert app.register_page.get_success_text() == Notice.SUCCESSFUL_ACTION

    def test_invalid_email_registration(self, app):
        app.register_page.open_register_page()
        data = InvalidEmailRegisterUserModel.random()
        app.register_page.invalid_email_register_user(data=data)
        assert app.register_page.get_error_text() ==\
               f"Error, {data.user} is not email address!"

    def test_invalid_password_registration(self, app):
        app.register_page.open_register_page()
        data = InvalidPasswordRegisterUserModel.random()
        app.register_page.invalid_password_register_user(data=data)
        assert app.register_page.get_error_text() == Notice.ERROR_DIFFERENT_PASS

    def test_short_password_registration(self, app):
        app.register_page.open_register_page()
        data = ShortPasswordRegisterUserModel.random()
        app.register_page.short_password_register_user(data=data)
        assert app.register_page.get_error_text() == Notice.ERROR_PASS_TOO_SHORT
