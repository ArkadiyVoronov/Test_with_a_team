import time

from fixtures.constants import Notice
from models.balance import BalanceUserModel


class TestBalancePage:
    def test_valid_balance(self, app, register_user):
        app.login_page.open_login_page()
        app.login_page.entry_data_login(register_user)
        time.sleep(1)
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.valid_balance(data=data)
        assert app.balance_page.get_success_text() == f"All good, you added {data.card_total} RUB to your account"

    def test_invalid_card_name(self, app, register_user):
        app.login_page.open_login_page()
        app.login_page.entry_data_login(register_user)
        time.sleep(1)
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        data.user = None
        app.balance_page.valid_balance(data=data)
        assert app.balance_page.get_error_text() == Notice.ERROR_NAME_BALANCE

    def test_invalid_card_number(self, app, register_user):
        app.login_page.open_login_page()
        app.login_page.entry_data_login(register_user)
        time.sleep(1)
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        data.card_number = "34563456345634"
        app.balance_page.valid_balance(data=data)
        assert app.balance_page.get_error_text() == Notice.ERROR_CARD_NUMBER

    def test_invalid_card_date(self, app, register_user):
        app.login_page.open_login_page()
        app.login_page.entry_data_login(register_user)
        time.sleep(1)
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        data.card_date = None
        app.balance_page.valid_balance(data=data)
        assert app.balance_page.get_error_text() == Notice.ERROR_CARD_DATE

    def test_invalid_money(self, app, register_user):
        app.login_page.open_login_page()
        app.login_page.entry_data_login(register_user)
        time.sleep(1)
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        data.card_total = None
        app.balance_page.valid_balance(data=data)
        assert app.balance_page.get_error_text() == Notice.ERROR_CARD_MONEY

    def test_invalid_checkbox(self, app, register_user):
        app.login_page.open_login_page()
        app.login_page.entry_data_login(register_user)
        time.sleep(1)
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.invalid_balance_checkbox(data=data)
        assert app.balance_page.get_error_text() == Notice.ERROR_CARD_CHECKBOX
