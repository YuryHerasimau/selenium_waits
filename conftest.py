from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selene import browser, support
import allure_commons
import allure
import pytest
import os
from faker import Faker
from pages.auth_page import LoginPage
from utils.urls import base_url


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-pipe")
    return options


@pytest.fixture()
def driver(chrome_options):
    if os.getenv("CI"): # Check if running on GitHub Actions
        print('driver', os.getenv("CI"))
        print('driver', os.getenv("CHROMEDRIVER_PATH"))
        chrome_driver_path = os.getenv("CHROMEDRIVER_PATH")
        service = Service(chrome_driver_path)
        service.start()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()  # autouse=True
def browser_management(chrome_options):
    if os.getenv("CI"): # Check if running on GitHub Actions
        print('browser_management', os.getenv("CI"))
        print('browser_management', os.getenv("CHROMEDRIVER_PATH"))
        chrome_driver_path = os.getenv("CHROMEDRIVER_PATH")
        service = Service(chrome_driver_path)
        service.start()
        # options = webdriver.Chrome(service=service)
    options = webdriver.ChromeOptions()
    browser.config.driver_options = options
    browser.config.window_width = 100
    browser.config.window_height = 500
    browser.config.timeout = 10

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=allure.attachment_type.PNG,
    )

    browser.quit()


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
