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
from Utils.Get_User_Input import *

load_dotenv()

PASSWORD = 12345678

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

num_accounts = int(get_user_input('How may users'))

for i in range(num_accounts):
    driver.get(os.getenv('DELIVERER'))

    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gOCSyD')))

    name_input = driver.find_element(By.NAME, 'name')
    name_input.send_keys(create_random_first_name())

    surname_input = driver.find_element(By.NAME, 'lastName')
    surname_input.send_keys(create_random_surname())

    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys(create_random_email())

    cpf_input = driver.find_element(By.NAME, 'cpf')
    cpf_input.send_keys(create_cpf())

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(PASSWORD)

    confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
    confirm_password_input.send_keys(PASSWORD)

driver.quit()