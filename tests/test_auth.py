from pages.auth_page import LoginPage
from utils.speed_test import speed_test
from utils.urls import base_url


def test_auth_positive(driver):
    page = LoginPage(driver, base_url)
    page.open()
    page.start_button().click()
    page.login_field().send_keys("login")
    page.password_field().send_keys("password")
    page.agree_button().click()
    page.registration_button().click()
    assert page.loader().is_displayed()
    assert page.success_message().text == "Вы успешно зарегистрированы!"
