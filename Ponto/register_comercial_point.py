"""
This module is used for creating X amount of "Pontos comerciais".
"""

import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

from Utils.get_user_input import get_user_input
from Utils.addres import create_address
from Utils.person import (
    create_random_full_name,
    create_phone,
    create_random_first_name,
    create_cnpj
)

# UTILS

load_dotenv()


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

num_accounts = int(get_user_input('How may users'))

for i in range(num_accounts):
    driver.get(os.getenv('POINT'))

    logo = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.gOCSyD')))

    name = driver.find_element(By.NAME, 'name')
    name.send_keys(create_random_full_name())

    phone = driver.find_element(By.NAME, 'phone')
    phone.send_keys(create_phone())

    comercial = driver.find_element(
        By.XPATH, '/html/body/main/div[2]/div/form/div/div[3]/div/label[2]')
    comercial.click()

    social = driver.find_element(By.NAME, 'company_name')
    social.send_keys(create_random_first_name())

    cnpj = driver.find_element(By.NAME, 'cnpj')
    cnpj.send_keys(create_cnpj())
    cnpj.submit()

    log_input = driver.find_element(By.NAME, 'street')
    log_input.send_keys(create_address()[0])

    number_input = driver.find_element(By.NAME, 'number')
    number_input.send_keys(create_address()[1])

    neighborhood_input = driver.find_element(By.NAME, 'neighborhood')
    neighborhood_input.send_keys('Bairro')

    city_input = driver.find_element(By.NAME, 'city')
    city_input.send_keys(create_address()[2])

    state_input = driver.find_element(By.NAME, 'uf')
    state_input.send_keys(create_address()[4])

    cep_input = wait.until(EC.element_to_be_clickable((By.ID, 'cep')))
    cep_input.send_keys(create_address()[3])
    cep_input.submit()

    time.sleep(0.5)

    print(i)

driver.quit()
