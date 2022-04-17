import logging
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.app import Application
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


@pytest.fixture
def app(request):
    url = request.config.getoption("--url")
    logger.info(f"Start app on {url}")
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    chrome_options.add_argument("window-size=1920,1080")
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
def register_user() -> RegisterUserModel:
    data = RegisterUserModel.random()
    body = {'username': data.user, 'password': data.password_1}
    req = requests.post('https://stores-tests-api.herokuapp.com/register', body)
    assert req.status_code == 201
    return data
