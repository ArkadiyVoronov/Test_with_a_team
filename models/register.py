from faker import Faker

fake = Faker()


class RegisterUserModel:
    def __init__(self, user: str=None, password_1: str=None, password_2: str=None):
        self.user = user
        self.password_1 = password_1
        self.password_2 = password_2

    @staticmethod
    def random():
        user = fake.email()
        password = fake.password()
        return RegisterUserModel(user=user, password_1=password, password_2=password)


class InvalidEmailRegisterUserModel:
    """Генерация фейковых данных для невалидной регистрации по email"""
    def __init__(self, user: str = None, password_1: str = None, password_2: str = None):
        self.user = user
        self.password_1 = password_1
        self.password_2 = password_2

    @staticmethod
    def random():
        user = fake.domain_name()
        password = fake.password()
        return InvalidEmailRegisterUserModel(user=user, password_1=password, password_2=password)


class InvalidPasswordRegisterUserModel:
    """Генерация фейковых данных для невалидной регистрации по паролю"""
    def __init__(self, user: str = None, password_1: str = None, password_2: str = None):
        self.user = user
        self.password_1 = password_1
        self.password_2 = password_2

    @staticmethod
    def random():
        user = fake.email()
        password_1 = fake.password()
        password_2 = fake.password()
        return InvalidPasswordRegisterUserModel(user=user, password_1=password_1, password_2=password_2)


class ShortPasswordRegisterUserModel:
    """Генерация фейковых данных для невалидной регистрации по паролю < 7 символов"""
    def __init__(self, user: str = None, password_1: str = None, password_2: str = None):
        self.user = user
        self.password_1 = password_1
        self.password_2 = password_2

    @staticmethod
    def random():
        user = fake.email()
        password = fake.password(length=6)
        return ShortPasswordRegisterUserModel(user=user, password_1=password, password_2=password)
