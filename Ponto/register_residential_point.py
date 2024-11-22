"""
This module is used for creating X amount of "Pontos residenciais".
"""

# Imports
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# Import env
from dotenv import load_dotenv

# Load scripts
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# Utils
from Utils.get_user_input import get_user_input

# Common
from Common.Web.logo_wait import wait_for_logo
from Common.Web.input_addres import input_addres
from Common.Web.person_input import (
    phone_input,
    name_input,
    cpf_input
)
from Common.Web.click_next_btn import click_next_btn


# Load env
load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

num_accounts = int(get_user_input('Qnt ponto'))

for i in range(num_accounts):
    driver.get(os.getenv('POINT'))

    wait_for_logo(wait)

    name_input(driver)

    phone_input(driver)

    try:
        residential = driver.find_element(By.CSS_SELECTOR, '.eEcEoS')
        ActionChains(driver).scroll_to_element(residential).perform()
        residential.click()
    except Exception as e:
        print('Error selectin the "residentio" option.\n', e)

    cpf_input(driver)
    
    click_next_btn(wait, driver)

    input_addres(wait, driver)

    print(i)

driver.quit()
