import time

from fixtures.constants import Notice
from models.balance import BalanceUserModel


class TestMainPage:
    def test_prepere_data_click(self, app, register_user):
        """
        Авторизуемся, пополняем баланс и добавляем товар в корзину.
        """
        app.login_page.open_login_page()
        app.login_page.entry_data_login(register_user.user, register_user.password_1)
        time.sleep(1)
        app.balance_page.open_balance_page()
        data = BalanceUserModel.random()
        app.balance_page.balance_transfer(data=data)
        app.main_page.open_main_page()
        if len(app.main_page.find_product()) > 0:
            app.main_page.add_product()
            assert app.main_page.get_success_text() == f"{app.main_page.find_product()} add to cart"
        else:
            app.main_page.load_store()
            app.main_page.open_main_page()
