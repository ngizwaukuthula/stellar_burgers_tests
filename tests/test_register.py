from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils import random_string

def test_register_user_with_correct_data():

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    login = random_string(8)
    email = random_string(8) + "@.yandex-team.ru"
    password = random_string(6)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, ".//label[text()='Имя']/parent::div/input[@type='text']")))
    name_input = driver.find_element(By.XPATH, ".//label[text()='Имя']/parent::div/input[@type='text']")
    name_input.send_keys(login)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, ".//label[text()='Email']/parent::div/input[@type='text']")))
    email_input = driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input[@type='text']")
    email_input.send_keys(email)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, ".//label[text()='Пароль']/parent::div/input[@type='password']")))
    password_input = driver.find_element(By.XPATH, ".//label[text()='Пароль']/parent::div/input[@type='password']")
    password_input.send_keys(password)

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Зарегистрироваться']")))
    register_button = driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']")
    register_button.click()

    WebDriverWait(driver, 3).until(lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/register")

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()

def test_rigister_user_with_incorrect_password():
   driver = webdriver.Chrome()
   driver.get("https://stellarburgers.nomoreparties.site/register")

   login = random_string(8)
   email = random_string(8) + "@.yandex-team.ru"
   password = random_string(5)

   WebDriverWait(driver, 3).until(
       expected_conditions.element_to_be_clickable(
           (By.XPATH, ".//label[text()='Имя']/parent::div/input[@type='text']")))
   name_input = driver.find_element(By.XPATH, ".//label[text()='Имя']/parent::div/input[@type='text']")
   name_input.send_keys(login)

   WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
       (By.XPATH, ".//label[text()='Email']/parent::div/input[@type='text']")))
   email_input = driver.find_element(By.XPATH, ".//label[text()='Email']/parent::div/input[@type='text']")
   email_input.send_keys(email)

   WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
       (By.XPATH, ".//label[text()='Пароль']/parent::div/input[@type='password']")))
   password_input = driver.find_element(By.XPATH, ".//label[text()='Пароль']/parent::div/input[@type='password']")
   password_input.send_keys(password)

   WebDriverWait(driver, 3).until(
       expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Зарегистрироваться']")))
   register_button = driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']")
   register_button.click()

   error_message = driver.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']")
   WebDriverWait(driver, 3).until(
      expected_conditions.visibility_of_element_located((By.XPATH, ".//p[@class='input__error text_type_main-default']")))

   assert error_message.text == 'Некорректный пароль'

   driver.quit()