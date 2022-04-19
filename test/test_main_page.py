import pytest
from selenium.common.exceptions import NoSuchElementException

from fixtures.constants import Notice


class TestMainPage:

    def test_add_product_to_basket(self, app):
        """
        Открываем главную страницу и проверяем, что карточки продуктов доступны для добавления в корзину.
        """
        app.main_page.open_main_page()
        try:
            app.main_page.find_product()
            app.main_page.add_product_to_basket()
            assert app.main_page.get_event_text() == f"{app.main_page.find_product()} add to cart"
        except NoSuchElementException():
            print("Отсутствуют продукты на главной странице")

    @pytest.mark.skip(reason="missing notification")
    def test_buy_empty_basket(self, app, update_balance):
        """
        Попытка купить, если корзина пуста.
        """
        app.main_page.load_store()
        app.main_page.open_basket()
        app.main_page.buy_product()
        assert app.main_page.get_event_text() == Notice.ERROR

    def test_error_small_balance(self, app, login_user):
        """
        Попытка купить, если недостаточный баланс.
        """
        app.main_page.load_store()
        app.main_page.add_product_to_basket()
        app.main_page.open_basket()
        [app.main_page.increase_products() for n in range(1, 5)]
        app.main_page.buy_product()
        assert app.main_page.check_error(Notice.ERROR)

    def test_success_shopping(self, app, update_balance):
        """Успешная покупка"""
        app.main_page.load_store()
        app.main_page.waiting_balance_update(update_balance.card_total)
        prod = app.main_page.find_product()
        app.main_page.add_product_to_basket()
        app.main_page.open_basket()
        app.main_page.buy_product()
        assert app.main_page.get_event_text() == f"Product {prod} buy sucess!"
