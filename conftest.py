import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.app import Application


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://berpress.github.io/react-shop/",
        help="products store",
    ),


@pytest.fixture
def app(request):
    url = request.config.getoption("--url")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)  # seconds
    app = Application(driver, url)
    yield app
    app.quit()


@pytest.fixture
def open_register_page(app):
    """Перед прохождением тестов открыть страницу Register."""
    app.register_page.open_register_page()




