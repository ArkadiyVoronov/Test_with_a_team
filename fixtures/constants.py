"""Константы, в т.ч. тексты ошибок и уведомлений."""


class Notice:
    SUCCESSFUL_ACTION = "Success"
    ERROR = "Erorr!"
    ERROR_CREDENTIALS = "Invalid credentials"
    ERROR_INVALID_EMAIL = "Error, tests is not email address!"
    ERROR_PASS_TOO_SHORT = "Password must be longer than 7 characters"
    ERROR_DIFFERENT_PASS = "Error, passwords do not match!"
    ERROR_NAME_BALANCE = "Check user name and last name! It must be not empty!"
    ERROR_CARD_NUMBER = "Check card number! It must be 16 symbols and not empty!"
    ERROR_CARD_DATE = "Check card date! It must be not empty!"
    ERROR_CARD_MONEY = "Check money! It must be not empty!"
    ERROR_CARD_CHECKBOX = "Read agree and click checkbox!"
