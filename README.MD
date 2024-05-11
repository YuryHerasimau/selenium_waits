# Selenium Waits Practice

This homework assignment focuses on practicing the use of waits in Selenium.

## Speed Testing Different Approaches

To assess the performance of various waiting mechanisms in Selenium, I utilized a `@speed_test` decorator. The decorator was used to measure the execution time of tests employing different waiting strategies:

- **Explicit Waits and Expected Conditions:** This approach involved waiting for specific conditions to be met before proceeding with test steps. The `@speed_test` decorator was instrumental in measuring the time taken for tests using Explicit Waits and Expected Conditions.

- **Implicit Waits:** Another method evaluated was Implicit Waits, where a global timeout is set for the WebDriver to wait for elements to be present in the DOM. The `@speed_test` decorator provided insights into the efficiency of this waiting strategy.

- **time.sleep():** Additionally, the traditional `time.sleep()` function was tested to observe its impact on test execution speed. The `@speed_test` decorator helped in quantifying the delay introduced by using this method.

By comparing the execution times of tests utilizing Explicit Waits, Implicit Waits, and `time.sleep()`, valuable insights were gained into the performance of each waiting mechanism. This analysis facilitated the identification of the most efficient approach for waiting in Selenium test automation.

### Test Case Details

- **Title:** Registration Functionality Check on the Website
- **Preconditions:** Browser is open, stable internet connection.

- **Steps:**
1. Open the specified URL of the website: [Selenium Waits Practice Site](https://victoretc.github.io/selenium_waits/)
2. Verify the title: Ensure that the text in the tag on the page matches "Практика с ожиданиями в Selenium"
3. Wait for the "Начать тестирование" button to appear.
4. Find the button: Locate the button with the text "Начать тестирование"
5. Start testing: Click on the "Начать тестирование" button.
6. Enter login: Input "login" into the login field.
7. Enter password: Input "password" into the password field.
8. Agree to the terms: Check the checkbox "Согласен со всеми правилами"
9. Confirm registration: Click the "Зарегистрироваться" button.
10. Check loading: Ensure that the loading indicator appears.
11. Check message: Verify that the message "Вы успешно зарегистрированы!" appears.

## Expected Result

The user successfully completes the registration process, sees the loading indicator, and receives the successful registration message.


### Success Criteria

The message "You have been successfully registered" is displayed on the screen.


## Getting Started

To use and run tests, follow these steps:

1. Clone the to your local machine using the following command:
```
git clone https://github.com/YuryHerasimau/selenium_waits.git
```
2. Navigate to the cloned repository directory on your local machine.
3. Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```
4. Activate the virtual environment by running the appropriate command based on your operating system. For Windows, you can use:
```
source env/Scripts/activate
```
5. Finally, run the tests using pytest with the following command:
```
pytest -s -v
```