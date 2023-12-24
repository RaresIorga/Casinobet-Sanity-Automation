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


@pytest.fixture(scope="module")
def setup_method():
    # Setup operations
    print("Starting")
    with SB(uc=True) as driver:
        # global driver
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.casinobet.com")
        yield driver
        time.sleep(10000)
        print("Ending")


def test_login_and_registration(setup_method):
    print("loginAndRegistration")
    driver = setup_method
    # clicking on register
    reglog.test_register_popup(driver)


def test_account_verification(setup_method):
    driver = setup_method
    # methods.account_registration(driver, "TestRares1112I01", "testrares114@gmail.com", "211RaresTest")
    # logging in
    methods.switch_to_email(driver, "testrares114@gmail.com", "danucapitanu23")
    methods.switch_to_email(driver, "testrares112@gmail.com", "danucapitanu23!")
    # needed a moment to load
    time.sleep(2)
    # verification in settings

