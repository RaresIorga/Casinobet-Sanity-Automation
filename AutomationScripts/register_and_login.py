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
import re


# Register pop-up functionality test.
def register_popup(driver):
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
    register_checkbox.click()
    # Verify that the Register button is not available until all the textboxes have been completed and the checkbox
    # is checked.
    register_button_popup = driver.find_element(By.XPATH, paths.register_button_popup_xpath)
    try:
        register_button_popup_clickable = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, paths.register_button_popup_xpath)))
        assert False
    except:
        assert True
    x_button = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.x_button)))
    x_button.click()


def account_verification(driver, email, password,get_verification_code=0):
    # if get_verification_code is 1 then the method will return the verification code extracted from the email.
    # logging into the email
    methods.switch_to_email(driver, email, password)
    # searching and verifying if the casinobet email has been sent
    time.sleep(5)
    try:
        casinobet_email = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, paths.gmail_casinobet_verification)))
        # clicking on the email and extracting the verification code
        casinobet_email.click()
    except:
        print("Verification Email has not been found")
        assert False
    if get_verification_code == 1:
        email_verification_code = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, paths.gmail_casinobet_verification_code)))
        verification_code_raw = email_verification_code.get_attribute("innerHTML")
        verification_code_numbers = re.findall(r'\d+', verification_code_raw)
        return verification_code_numbers
    driver.switch_to_window(0)


def settings_verification(driver, email, password, change_to_email, second_email, second_password):
    # clicking on profile
    header_profile = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.avatar_xpath)))
    header_profile.click()
    # clicking on settings
    settings = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.profile_settings)))
    settings.click()
    # clicking on verification
    verification = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.settings_verification)))
    verification.click()
    # Verify that the “Send” button is not available.
    send_buton = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.verification_send)))
    if send_buton.is_enabled():
        assert False
    # Verify that the user cannot verify his email with the wrong code.
    verification_code_digits_number = 7
    for i in range(1, verification_code_digits_number):
        verification_code_input = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, paths.verification_code + f"[{i}]")))
        verification_code_input.send_keys("0")
    send_buton.click()
    time.sleep(2)
    # Verify that the send again button works as intended.
    send_another_code = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.verification_request_another_code)))
    send_another_code.click()
    time.sleep(5)
    account_verification(driver, email, password)
    # Verify that the change email button works as intended.
    change_email = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.verification_specify_another_email)))
    change_email.click()
    another_email_input = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.verification_another_email_input)))
    another_email_input.send_keys(change_to_email)
    send_buton = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.verification_send)))
    send_buton.click()
    # Switching to email window to see if I receive the "Verify your email" on the new email
    verification_code = account_verification(driver, get_verification_code=1, email=second_email,
                                             password=second_password)
    verification_code_int = int(verification_code[0])
    driver.switch_to_window(0)
    back_button = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.back_button)))
    back_button.click()
    verification_code_input = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.verification_code + "[1]")))
    verification_code_input.send_keys(verification_code_int)
    send_buton = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.verification_send)))
    send_buton.click()
    x_button = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.settings_x_button)))
    x_button.click()


def password_verification(driver, username="TestRares1212I01", password="TestRares1212I01"):
    pass


def test_ciorna(driver, first_email="testrares114@gmail.com", second_email="testrares112@gmail.com",
                password="danucapitanu23!"):
    register_button = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.register_button_xpath)))
    register_button.click()
    try:
        register_button_popup_clickable = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, paths.register_button_popup_xpath)))
        assert False
    except:
        assert True
