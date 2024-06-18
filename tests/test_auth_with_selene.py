from selene import browser, by, be, have
from selene.support.shared.jquery_style import s, ss
from selenium import webdriver
import allure
import time


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
browser.config.driver_options = options
browser.config.timeout = 10
# browser.config.window_width = 100
# browser.config.window_height = 500


@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://victoretc.github.io/selenium_waits/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_login():

    with allure.step('Открыть главную страницу'):
        browser.open("https://victoretc.github.io/selenium_waits/")

    browser.element('//*[@id="startTest"]').click()
    # browser.element(by.xpath('//*[@id="startTest"]')).with_(timeout=10).click()
    # s('//*[@id="startTest"]').click()
    s('#login').type('John')
    s('#password').type('password123')
    s('#agree').click()
    browser.element(by.text('Зарегистрироваться')).click()
    s('#successMessage').should(have.text('Вы успешно зарегистрированы!'))