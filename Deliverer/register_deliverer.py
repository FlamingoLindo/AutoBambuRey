from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import sys
from dotenv import load_dotenv

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# UTILS
from Utils.person import *
from Utils.addres import *

load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get(os.getenv('INFLUENCER'))

logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gOCSyD')))

name_input = driver.find_element(By.NAME, 'name')
name_input.send_keys(create_random_first_name())

email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys(create_random_email())

phone_input = driver.find_element(By.NAME, 'phone')
phone_input.send_keys(create_phone())
phone_input.submit()



time.sleep(10)
driver.quit()