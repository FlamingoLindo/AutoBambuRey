"""
This module is used for creating X amount of "Entregador" users.
"""

import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

from Utils.get_user_input import get_user_input
from Utils.addres import create_address
from Utils.person import (
    create_random_email,
    create_random_first_name,
    create_random_surname,
    create_cpf
)


path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# UTILS

load_dotenv()

PASSWORD = 12345678

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

num_accounts = int(get_user_input('How may users'))

for i in range(num_accounts):
    driver.get(os.getenv('DELIVERER'))

    logo = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.gOCSyD')))

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
    confirm_password_input.submit()

    log_input = wait.until(EC.element_to_be_clickable((By.NAME, 'street')))
    log_input.send_keys(create_address()[0])

    number_input = driver.find_element(By.NAME, 'number')
    number_input.send_keys(create_address()[1])

    neighborhood_input = driver.find_element(By.NAME, 'neighborhood')
    neighborhood_input.send_keys('Bairro')

    city_input = driver.find_element(By.NAME, 'city')
    city_input.send_keys(create_address()[2])

    state_input = driver.find_element(By.NAME, 'uf')
    state_input.send_keys(create_address()[4])

    cep_input = wait.until(EC.element_to_be_clickable((By.NAME, 'cep')))
    cep_input.send_keys(create_address()[3])
    cep_input.submit()

    time.sleep(0.5)

    print(i)

driver.quit()
