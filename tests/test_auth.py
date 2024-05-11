def test_auth_positive(login_page):
    login_page.open()
    login_page.start_button().click()
    login_page.login_field().send_keys("login")
    login_page.password_field().send_keys("password")
    login_page.agree_button().click()
    login_page.registration_button().click()
    assert login_page.loader().is_displayed()
    assert login_page.success_message().text == "Вы успешно зарегистрированы!"
