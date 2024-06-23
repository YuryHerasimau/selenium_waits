from pages import auth_with_selene
import allure
from utils.speed_test import speed_test
from utils.urls import base_url


@allure.title("Test Authentication")
@allure.description(
    "This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication."
)
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link(base_url, name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@speed_test
def test_login(browser_management, fake_login, fake_password):

    with allure.step("Открыть главную страницу"):
        auth_with_selene.visit(base_url)

    auth_with_selene.start().click()
    auth_with_selene.login(fake_login, fake_password)
    auth_with_selene.success_message_have_text("Вы успешно зарегистрированы!")
