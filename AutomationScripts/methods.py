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


def login_email(email, password):
    with SB(uc=True) as driver:
        driver.get("https://www.gmail.com")
        # login_with_google = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.stackoverflow_signin_google)))
        # login_with_google.click()
        # google_reject_cookies = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.google_reject_cookies)))
        # google_reject_cookies.click()
        # google_signin_button = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.google_signin)))
        # google_signin_button.click()
        email_textbox = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_email_textbox)))
        email_textbox.send_keys(email)
        next = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_next_btn)))
        next.click()
        time.sleep(10)
        password_textbox = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_password_textbox)))
        password_textbox.send_keys(password)
        next = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.gmail_next_btn)))
        next.click()
        # nu_acum = driver.find_element(By.XPATH, paths.gmail_nu_acum)
        # nu_acum.click()
        time.sleep(10)

def login_email_github(email, password):
    with SB(uc=True) as driver:
        driver.get(
            "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
        driver.type("#identifierId",email)
        driver.click("#identifierNext > div > button")

        driver.type("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input", password)
        driver.click("#passwordNext > div > button")
        time.sleep(10)
def account_registration(driver, username, email, password):
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
