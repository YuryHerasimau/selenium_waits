from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selene import browser, support
import allure_commons
import allure
import pytest
from faker import Faker

from pages.auth_page import LoginPage
from utils.urls import base_url


@pytest.fixture
def chrome_options():
    # options = Options()
    options = webdriver.ChromeOptions()
    browser.config.driver_options = options
    # options.add_argument("--headless")
    # options.add_argument("--start-maximized")
    browser.config.window_width = 100
    browser.config.window_height = 500
    browser.config.timeout = 10

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    return options


@pytest.fixture(autouse=True)
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )

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


@pytest.fixture
def login_page(driver):
    return LoginPage(driver, base_url)
