from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils import *

def test_log_out_by_clicking_exit_button():
    login, email, password = register_random_user()

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    try_to_log_in(driver, email, password)

    WebDriverWait(driver, 3).until(
        lambda driver: driver.current_url == "https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a[@href='/account']")))
    account_link = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']/parent::a[@href='/account']")
    account_link.click()

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Выход']")))
    exit_button = driver.find_element(By.XPATH, ".//button[text()='Выход']")
    exit_button.click()

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, ".//button[text()='Войти']")))
    enter_button = driver.find_element(By.XPATH, ".//button[text()='Войти']")

    assert enter_button.is_displayed() and enter_button.is_enabled()

    driver.quit()