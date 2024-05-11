from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from faker import Faker


@pytest.fixture
def chrome_options():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


@pytest.fixture
def fake_login():
    fake = Faker()
    return fake.name()


@pytest.fixture
def fake_password():
    fake = Faker()
    return fake.text()
