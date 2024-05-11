from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from speed_test import speed_test


BASE_URL = 'https://victoretc.github.io/selenium_waits/'


# See also: https://github.com/victoretc/selenium_automation_course/blob/main/lesson3/readme.md

@speed_test
def test_register_with_explicit_waits(driver, wait, fake_login, fake_password):
    """Using Explicit waits and Expected Conditions"""
    driver.get(BASE_URL)
    actual_title = driver.find_element(By.XPATH, '/html/body/h1').text
    expected_title = "Практика с ожиданиями в Selenium"
    assert actual_title == expected_title, f"Page title doesn't match. Actual: {actual_title}. Expected: {expected_title}"

    start_test_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="startTest"]')))
    assert start_test_button.is_displayed()
    expected_text = "Начать тестирование"
    assert start_test_button.text == expected_text, f"Button text doesn't match. Actual: {start_test_button.text}. Expected: {expected_text}"

    start_test_button.click()
    driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(fake_login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(fake_password)
    driver.find_element(By.XPATH, '//*[@id="agree"]').click()
    driver.find_element(By.XPATH, '//*[@id="register"]').click()
    loader = driver.find_element(By.XPATH, '//*[@id="loader"]')
    assert loader.is_displayed()

    success_message = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="successMessage"]')))
    expected_success_message = "Вы успешно зарегистрированы!"
    assert success_message.text == expected_success_message, f"Success message text doesn't match. Actual: {success_message.text}. Expected: {expected_success_message}"


@speed_test
def test_register_with_implicit_waits(driver, wait, fake_login, fake_password):
    """Using Implicit waits"""
    driver.get(BASE_URL)
    actual_title = driver.find_element(By.XPATH, '/html/body/h1').text
    expected_title = "Практика с ожиданиями в Selenium"
    assert actual_title == expected_title, f"Page title doesn't match. Actual: {actual_title}. Expected: {expected_title}"

    start_test_button = driver.find_element(By.XPATH, '//*[@id="startTest"]')
    start_test_button.click() # костыль
    assert start_test_button.is_displayed()
    expected_text = "Начать тестирование"
    assert start_test_button.text == expected_text, f"Button text doesn't match. Actual: {start_test_button.text}. Expected: {expected_text}"

    start_test_button.click()
    driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(fake_login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(fake_password)
    driver.find_element(By.XPATH, '//*[@id="agree"]').click()
    driver.find_element(By.XPATH, '//*[@id="register"]').click()
    loader = driver.find_element(By.XPATH, '//*[@id="loader"]')
    assert loader.is_displayed()

    success_message = driver.find_element(By.XPATH, '//*[@id="successMessage"]')
    success_message.click() # костыль
    expected_success_message = "Вы успешно зарегистрированы!"
    assert success_message.text == expected_success_message, f"Success message text doesn't match. Actual: {success_message.text}. Expected: {expected_success_message}"


@speed_test
def test_register_with_time_sleep(driver, wait, fake_login, fake_password):
    """Using time.sleep()"""
    driver.get(BASE_URL)
    actual_title = driver.find_element(By.XPATH, '/html/body/h1').text
    expected_title = "Практика с ожиданиями в Selenium"
    assert actual_title == expected_title, f"Page title doesn't match. Actual: {actual_title}. Expected: {expected_title}"

    start_test_button = driver.find_element(By.XPATH, '//*[@id="startTest"]')
    time.sleep(5)
    assert start_test_button.is_displayed()
    expected_text = "Начать тестирование"
    assert start_test_button.text == expected_text, f"Button text doesn't match. Actual: {start_test_button.text}. Expected: {expected_text}"

    start_test_button.click()
    driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(fake_login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(fake_password)
    driver.find_element(By.XPATH, '//*[@id="agree"]').click()
    driver.find_element(By.XPATH, '//*[@id="register"]').click()
    loader = driver.find_element(By.XPATH, '//*[@id="loader"]')
    assert loader.is_displayed()

    time.sleep(3)
    success_message = driver.find_element(By.XPATH, '//*[@id="successMessage"]')
    expected_success_message = "Вы успешно зарегистрированы!"
    assert success_message.text == expected_success_message, f"Success message text doesn't match. Actual: {success_message.text}. Expected: {expected_success_message}"
