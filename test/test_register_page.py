import time

from fixtures.constants import Notice
import pytest


class TestRegisterPage:

    @pytest.fixture
    def open_register_page(self):
        #self.app.driver.get(self.app.url)
        app.register_page.open_register_page()
        """Перед прохождением тестов открыть страницу Register."""

    def test_invalid_email(self, app):
        """
        1. Указать некорректную почту
        2. Нажать Register
        """
        time.sleep(5)
        app.register_page.fill_in_email("test")
        assert app.register_page.get_error_text() == Notice.ERROR_INVALID_EMAIL

    def test_too_short_pass(self, app):
        """
        1. Указать короткий пароль
        2. Нажать Register
        """
        app.register_page.fill_in_password1("111")
        assert app.register_page.get_error_text() == Notice.ERROR_PASS_TOO_SHORT

    def test_different_pass(self, app):
        """
        1. Указать пароль
        2. Нажать Register
        """
        app.register_page.fill_in_password1("111")
        app.register_page.fill_in_password2("222")
        assert app.register_page.get_error_text() == Notice.ERROR_PASS_TOO_SHORT

"""
//div[@class='card-panel red lighten-2']
 успешная регистрация - всплывающее уведомление Success //div[@class='toast']
"""