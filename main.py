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

from AutomationScripts import RegisterAndLogin as reglog

@pytest.fixture(scope="module")
def setup_method():
    # Setup operations
    print("Starting")
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.casinobet.com")
    yield driver
    print("Ending")
    driver.quit()


def test_loginandregistration(setup_method):
    print("loginAndRegistration")
    # clicking on register
    reglog.test_Register_popup(driver)