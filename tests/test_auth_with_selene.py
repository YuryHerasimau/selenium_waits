from selene import browser, by, be, have
from selene.support.shared.jquery_style import s, ss
from selenium import webdriver
import allure
import time

from utils.speed_test import speed_test
from utils.urls import base_url


@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link(base_url, name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@speed_test
def test_login():

    with allure.step('Открыть главную страницу'):
        browser.open(base_url)

    browser.element('//*[@id="startTest"]').click()
    # browser.element(by.xpath('//*[@id="startTest"]')).with_(timeout=10).click()
    # s('//*[@id="startTest"]').click()
    s('#login').type('John')
    s('#password').type('password123')
    s('#agree').click()
    browser.element(by.text('Зарегистрироваться')).click()
    s('#successMessage').should(have.text('Вы успешно зарегистрированы!'))