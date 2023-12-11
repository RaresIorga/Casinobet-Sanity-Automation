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

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.casinobet.com")

register_button = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, paths.register_button_xpath)))
register_button.click()
register_button_popup = driver.find_element(By.XPATH, paths.register_button_popup_xpath)
inner_html = register_button_popup.get_attribute("innerHTML")
print(inner_html)