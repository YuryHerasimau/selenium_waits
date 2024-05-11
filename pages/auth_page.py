from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    _start_button = (By.XPATH, '//*[@id="startTest"]')
    _login_field = (By.XPATH, '//*[@id="login"]')
    _password_field = (By.XPATH, '//*[@id="password"]')
    _agree_button = (By.XPATH, '//*[@id="agree"]')
    _registration_button = (By.XPATH, '//*[@id="register"]')
    _loader = (By.XPATH, '//*[@id="loader"]')
    _success_message = (By.XPATH, '//*[@id="successMessage"]')

    def start_button(self):
        return self.is_visible(LoginPage._start_button)

    def login_field(self):
        return self.is_visible(LoginPage._login_field)

    def password_field(self):
        return self.is_visible(LoginPage._password_field)

    def agree_button(self):
        return self.is_visible(LoginPage._agree_button)

    def registration_button(self):
        return self.is_visible(LoginPage._registration_button)

    def loader(self):
        return self.is_visible(LoginPage._loader)

    def success_message(self):
        return self.is_visible(LoginPage._success_message)
