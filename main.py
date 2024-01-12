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

username = "TestRares1001I01"
password = "211RaresTest"

@pytest.fixture(scope="module")
def setup_method():
    # Setup operations
    print("Starting")
    with SB(uc=True) as driver:
        driver.get("https://www.casinobet.com")
        yield driver
        time.sleep(10000)
        print("Ending")


def test_login_and_registration(setup_method):
    print("loginAndRegistration")
    driver = setup_method
    # testing the register and login pop-up
    reglog.register_popup(driver)
    methods.account_registration(driver, username, password)


def test_account_verification(setup_method):
    driver = setup_method
    methods.login(driver, "TestRares1212I01", "211RaresTest")

