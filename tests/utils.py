from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import string
import random
def random_string(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def register_random_user():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    login = random_string(8)
    email = random_string(8) + "@.yandex-team.ru"
    password = random_string(6)

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

    WebDriverWait(driver, 3).until(
        lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/register")

    driver.quit()

    return login, email, password

def try_to_log_in(driver, email, password):
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//input[@type='text']")))
    email_input = driver.find_element(By.XPATH, ".//input[@type='text']")

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//input[@type='password']")))
    password_input = driver.find_element(By.XPATH, ".//input[@type='password']")

    email_input.send_keys(email)
    password_input.send_keys(password)

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))
    enter_button = driver.find_element(By.XPATH, ".//button[text()='Войти']")


    enter_button.click()

    WebDriverWait(driver, 3).until(
        lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/login")
