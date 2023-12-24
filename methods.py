from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import paths
from seleniumbase import SB


def siteAccess():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.casinobet.com")

    input("Press any key to exit\n")
    driver.quit()


def switch_to_email(driver, email, password):
    # switching to a new tab and entering gmail
    driver.execute_script("window.open('');")
    num_tabs = len(driver.driver.window_handles)
    driver.switch_to_window(num_tabs - 1)
    driver.get("https://www.gmail.com")
    # verifying if the user is already logger in with the correct account
    try:
        # is_signed_in will search for the "Sign In" message at the login window"
        is_signed_in = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, paths.gmail_is_signed)))
        email_textbox = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, paths.gmail_email_textbox)))
        email_textbox.send_keys(email)
        next = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_next_btn)))
        next.click()
        password_textbox = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH, paths.gmail_password_textbox)))
        password_textbox.send_keys(password)
        next = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_next_btn)))
        next.click()
    except:
        # if the user is signed in, it will verify that he is logged in with the correct account
        try:
            same_account_verify = WebDriverWait(driver, 200).until(
                EC.presence_of_element_located((By.XPATH, paths.get_path_gmail_account(email))))
        except:
            # if not, the account will be changed
            gmail_account_button = WebDriverWait(driver, 200).until(
                EC.presence_of_element_located((By.XPATH, paths.gmail_account_button)))
            gmail_account_button.click()
            iframe = WebDriverWait(driver, 200).until(
                EC.presence_of_element_located((By.XPATH, paths.gmail_account_iframe)))
            time.sleep(2)
            driver.switch_to_frame(iframe)
            gmail_add_another_account = WebDriverWait(driver, 500).until(
                EC.presence_of_element_located((By.XPATH, paths.gmail_add_another_acount)))
            gmail_add_another_account.click()
            # selecting the latest tab
            driver.switch_to_window(num_tabs)
            email_textbox = WebDriverWait(driver, 200).until(
                EC.presence_of_element_located((By.XPATH, paths.gmail_email_textbox)))
            email_textbox.send_keys(email)
            next = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_next_btn)))
            next.click()
            password_textbox = WebDriverWait(driver, 200).until(
                EC.presence_of_element_located((By.XPATH, paths.gmail_password_textbox)))
            password_textbox.send_keys(password)
            next = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_next_btn)))
            next.click()




def account_registration(driver, username, email, password, country="Romania"):
    register_button = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.register_button_xpath)))
    register_button.click()
    # finding the textbox
    register_username = driver.find_element(By.XPATH, paths.register_username)
    register_email = driver.find_element(By.XPATH, paths.register_email)
    register_password = driver.find_element(By.XPATH, paths.register_password)
    # writing in textbox
    register_username.send_keys(username)
    register_email.send_keys(email)
    register_password.send_keys(password)
    register_checkbox = driver.find_element(By.XPATH, paths.register_checkbox)
    register_checkbox.click()
    # registering the account
    register_button_popup = driver.find_element(By.XPATH, paths.register_button_popup_xpath)
    register_button_popup.click()
    # selecting the country
    country_select = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.country_select_xpath)))
    country_select.click()
    country_search = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.country_search_xpath)))
    country_search.send_keys(country)
    country_option_select = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.country_option_select_xpath)))
    country_option_select.click()
    country_submit = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.country_submit_xpath)))
    country_submit.click()


def login(driver, username, password):
    login_button = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.login_button)))
    login_button.click()
    login_username = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.login_username)))
    login_username.send_keys(username)
    login_password = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.login_password)))
    login_password.send_keys(password)
    login_submit = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, paths.login_submit)))
    login_submit.click()
