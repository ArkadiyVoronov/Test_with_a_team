from models.register import RegisterUserModel


class TestRegisterPage:

    # def test_invalid_email(self, app):
    #     """
    #     1. Указать некорректную почту
    #     2. Нажать Register
    #     """
    #     app.register_page.open_register_page()
    #     app.register_page.fill_in_email("test")
    #     assert app.register_page.get_error_text()
    #     == Notice.ERROR_INVALID_EMAIL
    #
    # def test_too_short_pass(self, app):
    #     """
    #     1. Указать короткий пароль
    #     2. Нажать Register
    #     """
    #     app.register_page.open_register_page()
    #     app.register_page.fill_in_password1("111")
    #     assert app.register_page.get_error_text()
    #     == Notice.ERROR_PASS_TOO_SHORT
    #
    # def test_different_pass(self, app):
    #     """
    #     1. Указать пароль
    #     2. Нажать Register
    #     """
    #     app.register_page.open_register_page()
    #     app.register_page.fill_in_password1("111")
    #     app.register_page.fill_in_password2("222")
    #     assert app.register_page.get_error_text()
    #     == Notice.ERROR_PASS_TOO_SHORT

    def test_valid_registration(self, app):
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        # data.user = None
        app.register_page.register_user(data=data)

# начать разгоняться
