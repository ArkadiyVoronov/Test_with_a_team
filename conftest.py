import logging
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.app import Application
from models.balance import BalanceUserModel
from models.register import RegisterUserModel

logger = logging.getLogger("react_shop")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://berpress.github.io/react-shop/",
        help="products store",
    ),
    parser.addoption("--headless", action="store_true", help="Headless mode"),
    parser.addoption("--api_url", action="store", default="https://stores-tests-api.herokuapp.com/register",
                     help="store API"),


@pytest.fixture
def app(request):
    url = request.config.getoption("--url")
    logger.info(f"Start app on {url}")
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    chrome_options.add_argument("window-size=1800,1080")
    if headless:
        chrome_options.headless = True
    else:
        chrome_options.headless = False
    driver = webdriver.Chrome(ChromeDriverManager().install(),
                              options=chrome_options)
    app = Application(driver, url)
    yield app
    app.quit()


@pytest.fixture(scope="class")
def register_user(request) -> RegisterUserModel:
    """Фикстура регистрации пользователя. Одна на класс."""
    data = RegisterUserModel.random()
    body = {'username': data.user, 'password': data.password_1}
    url = request.config.getoption("--api_url")
    req = requests.post(url, body)
    assert req.status_code == 201
    logger.info(f"Registered user {data.user} pass = {data.password_1}")
    return data


@pytest.fixture()
def login_user(app, register_user):
    """Фикстура авторизации пользователя."""
    app.login_page.open_login_page()
    app.login_page.entry_data_login(register_user.user, register_user.password_1)
    app.login_page.wait_notice()


@pytest.fixture()
def update_balance(app, login_user):
    """Фикстура пополнения баланса пользователя."""
    app.balance_page.open_balance_page()
    data = BalanceUserModel.random()
    app.balance_page.balance_transfer(data=data)
    app.balance_page.wait_notice()
    return data
