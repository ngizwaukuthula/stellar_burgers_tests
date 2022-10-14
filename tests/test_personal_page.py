from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import string

from utils import *

def test_enter_personal_page_for_lgged_out_user():

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a[@href='/account']")))
    account_link = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']/parent::a[@href='/account']")
    account_link.click()

    WebDriverWait(driver, 3).until(
        lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/")

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()

def test_enter_personal_page_for_lgged_in_user():

    login, email, password = register_random_user()

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти в аккаунт']")))
    login_button = driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']")
    login_button.click()

    WebDriverWait(driver, 3).until(
        lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/")

    try_to_log_in(driver, email, password)

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a[@href='/account']")))

    account_link = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']/parent::a[@href='/account']")

    account_link.click()

    WebDriverWait(driver, 30).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, ".//button[text()='Выход']")))
    exit_button = driver.find_element(By.XPATH, ".//button[text()='Выход']")

    driver.execute_script("arguments[0].scrollIntoView();", exit_button)

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile" \
           and exit_button.is_displayed()

    driver.quit()