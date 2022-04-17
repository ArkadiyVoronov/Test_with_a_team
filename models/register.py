from faker import Faker

fake = Faker()


class RegisterUserModel:
    def __init__(self, user: str = None, password_1: str = None, password_2: str = None, domain: str = None):
        self.user = user
        self.password_1 = password_1
        self.password_2 = password_2
        self.domain = domain

    @staticmethod
    def random():
        user = fake.email()
        password = fake.password()
        domain = fake.domain_name()
        return RegisterUserModel(user=user, password_1=password, password_2=password, domain=domain)
