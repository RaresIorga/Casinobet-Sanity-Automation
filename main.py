from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import paths
import methods
import time
from seleniumbase import SB

from AutomationScripts import register_and_login as reglog

username = "TestRaresAuto10"
password = "211RaresTest"
register_email = f"testrares114+{username}@gmail.com"
change_to_email = f"testrares112+{username}@gmail.com"
email = "testrares114@gmail.com"
email_password = "danucapitanu23"
second_email = "testrares112@gmail.com"
second_email_password = "danucapitanu23!"
@pytest.fixture(scope="module")
def setup_method():
    # Setup operations
    print("Starting")
    with SB(uc=True) as driver:
        driver.get("https://www.casinobet.com")
        yield driver
        # time sleep needs to be removed at the end
        time.sleep(10000)
        print("Ending")


def test_login_and_registration_pop(setup_method):
    print("loginAndRegistration")
    driver = setup_method
    # testing the register and login pop-up
    reglog.register_popup(driver)

def test_account(setup_method):
    driver = setup_method
    # registering an account
    methods.account_registration(driver, username=username, password=password, email=register_email)
    # verifying that the verification email has been sent
    reglog.account_verification(driver, email=email, password=email_password)
    # verifying everything settings related
    reglog.settings_verification(driver, email=email, password=email_password, change_to_email=change_to_email,
                                 second_email=second_email, second_password=second_email_password)


# def test_ciorna(setup_method):
#     driver = setup_method
#     reglog.test_ciorna(driver)
