from faker import Faker
import random
from typing import Any

fake = Faker()


class BalanceUserModel:
    """Генерация фейковых данных для валидной операции пополнения баланка карты."""

    def __init__(self, user: str = None, card_number: str = None, card_date: str = None, card_total: str = None):
        self.user = user
        self.card_number = card_number
        self.card_date = card_date
        self.card_total = card_total

    @staticmethod
    def random():
        user = fake.name()
        card = fake.credit_card_number(card_type='mastercard')
        date = fake.date(pattern="%Y/%m")
        total = str(random.randint(100, 1000))

        return BalanceUserModel(user=user, card_number=card, card_date=date, card_total=total)
