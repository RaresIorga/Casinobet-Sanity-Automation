from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# navigating to the webpage
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.casinobet.com")

input("Press any key to exit\n")
driver.quit()