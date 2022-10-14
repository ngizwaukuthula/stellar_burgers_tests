from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import string
from utils import *

def test_login_on_mane_page():
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
        expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Оформить заказ']")))
    new_order_button = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")

    assert new_order_button.is_enabled()

    driver.quit()

def test_login_on_personal_page():
    login, email, password = register_random_user()

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a[@href='/account']")))
    login_link = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']/parent::a[@href='/account']")
    login_link.click()

    WebDriverWait(driver, 3).until(
        lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/")

    try_to_log_in(driver, email, password)

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Оформить заказ']")))
    new_order_button = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")

    assert new_order_button.is_enabled()

    driver.quit()

def test_login_on_register_page():

    login, email, password = register_random_user()

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//a[@href='/login']")))
    login_link = driver.find_element(By.XPATH, ".//a[@href='/login']")
    login_link.click()

    WebDriverWait(driver, 3).until(
        lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/register")

    try_to_log_in(driver, email, password)

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Оформить заказ']")))
    new_order_button = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")

    assert new_order_button.is_enabled()

    driver.quit()

def test_login_on_restore_passwrod_page():
    login, email, password = register_random_user()

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//a[@href='/login']")))
    login_link = driver.find_element(By.XPATH, ".//a[@href='/login']")
    login_link.click()

    WebDriverWait(driver, 3).until(
        lambda driver: driver.current_url != "https://stellarburgers.nomoreparties.site/forgot-password")

    try_to_log_in(driver, email, password)

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Оформить заказ']")))
    new_order_button = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")

    assert new_order_button.is_enabled()

    driver.quit()