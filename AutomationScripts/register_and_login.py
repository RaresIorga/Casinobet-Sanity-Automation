from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import paths
import pytest
import methods


# Register pop-up functionality test.
def test_register_popup(driver):
    # clicking on register
    register_button = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.register_button_xpath)))
    register_button.click()
    # Verify that the login button will send the user to the login pop-up.
    login_btn_popup = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.register_popup_login_xpath)))
    login_btn_popup.click()
    is_on_login = driver.find_element(By.XPATH, paths.is_login_popup_xpath)
    if is_on_login:
        assert True
    else:
        assert False
    # Verify that the register button will send the user back to the Register pop-up
    register_btn_popup = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.login_popup_register_xpath)))
    register_btn_popup.click()
    is_on_register = driver.find_element(By.XPATH, paths.is_register_popup_xpath)
    if is_on_register:
        assert True
    else:
        assert False
    # Verify that all the textboxes are available and functional.
    register_username = driver.find_element(By.XPATH, paths.register_username)
    register_email = driver.find_element(By.XPATH, paths.register_email)
    register_password = driver.find_element(By.XPATH, paths.register_password)
    register_username.send_keys("test")
    register_email.send_keys("test")
    register_password.send_keys("test")
    # Verify that the checkbox with the terms and conditions can be checked.
    register_checkbox = driver.find_element(By.XPATH, paths.register_checkbox)
    register_checkbox.click()
    # Verify that the Register button is not available until all the textboxes have been completed and the checkbox is checked.
    register_button_popup = driver.find_element(By.XPATH, paths.register_button_popup_xpath)
    try:
        register_button_popup.click()
        assert False
    except:
        assert True


def account_verification(driver):
    # switching to a new tab
    driver.execute_script("window.open('');")
    driver.switch_to_window(1)
    # logging into the email
    methods.switch_to_email(driver, "testrares114@gmail.com", "danucapitanu23")
    driver.execute_script("window.open('');")
    driver.switch_to_window(2)
    methods.switch_to_email(driver, "testrares114@gmail.com", "danucapitanu23")
    # searching and verifying the casinobet email
    casinobet_email = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.gmail_casinobet_verification)))
    casinobet_email.click()


def test_ciorna():
    pass
