from fixtures.constants import Notice
from models.register import RegisterUserModel


class TestLoginPage:

    def test_successful_login(self, app, register_user):
        app.login_page.open_login_page()
        app.login_page.entry_data_login(register_user.user, register_user.password_1)
        assert app.login_page.get_event_text() == Notice.SUCCESSFUL_ACTION

    def test_login_with_invalid_password(self, app, register_user):
        app.login_page.open_login_page()
        app.login_page.entry_data_login(register_user.user, '123')
        assert app.login_page.get_event_text() == Notice.ERROR_CREDENTIALS

    def test_login_with_empty_password(self, app, register_user):
        app.login_page.open_login_page()
        app.login_page.entry_data_login(register_user.user, None)
        assert app.login_page.get_event_text() == Notice.ERROR_CREDENTIALS

    def test_login_with_invalid_user(self, app, register_user):
        app.login_page.open_login_page()
        invalid_email = '1'+register_user.user
        app.login_page.entry_data_login(invalid_email, register_user.password_1)
        assert app.login_page.get_event_text() == Notice.ERROR_CREDENTIALS

    def test_non_existent_user(self, app):
        app.login_page.open_login_page()
        non_exist_user = RegisterUserModel.random()
        app.login_page.entry_data_login(non_exist_user.user, non_exist_user.password_1)
        assert app.login_page.get_event_text() == Notice.ERROR_CREDENTIALS
