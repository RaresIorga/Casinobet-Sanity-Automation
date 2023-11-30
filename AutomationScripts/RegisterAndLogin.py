from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import paths

def Register(driver):
    register_button = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.register_button_xpath)))
    register_button.click()
