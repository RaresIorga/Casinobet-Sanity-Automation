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
        try:
            driver.get("https://www.gmail.com")
            is_signed_in = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, paths.gmail_is_signed)))
            email_textbox = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_email_textbox)))
            email_textbox.send_keys(email)
            next = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_next_btn)))
            next.click()
            time.sleep(10)
            password_textbox = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_password_textbox)))
            password_textbox.send_keys(password)
            next = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_next_btn)))
            next.click()
        except:
            time.sleep(60)



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
