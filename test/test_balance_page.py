import time
from fixtures.constants import Notice
from models.balance import BalanceUserModel


class TestBalancePage:
    def test_balance_transfer(self, app, login_user):
        """
        Пополнение баланса.
        """
        time.sleep(1)  # TODO: как избавиться от ожидания
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.balance_transfer(data=data)
        assert app.balance_page.get_success_text() == f"All good, you added {data.card_total} RUB to your account"

    def test_empty_card_name(self, app, login_user):
        """
        Пополнение баланса без заполнения имени держателя карты.
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        data.user = None
        app.balance_page.balance_transfer(data=data)
        assert app.balance_page.get_error_text() == Notice.ERROR_NAME_BALANCE

    def test_empty_card_number(self, app, login_user):
        """
        Пополнение баланса без заполнения номера карты.
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        data.card_number = "34563456345634"
        app.balance_page.balance_transfer(data=data)
        assert app.balance_page.get_error_text() == Notice.ERROR_CARD_NUMBER

    def test_empty_card_date(self, app, login_user):
        """
        Пополнение баланса без заполнения даты действия карты.
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        data.card_date = None
        app.balance_page.balance_transfer(data=data)
        assert app.balance_page.get_error_text() == Notice.ERROR_CARD_DATE

    def test_empty_money(self, app, login_user):
        """
        Пополнение баланса без заполнения суммы.
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        data.card_total = None
        app.balance_page.balance_transfer(data=data)
        assert app.balance_page.get_error_text() == Notice.ERROR_CARD_MONEY

    def test_empty_checkbox(self, app, login_user):
        """
        Пополнение баланса без принятия правил(чекбокс).
        """
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.balance_transfer(data=data, is_agree=False)
        assert app.balance_page.get_error_text() == Notice.ERROR_CARD_CHECKBOX
