"""
This module is used for creating X amount of "Pontos comerciais".
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

# UTILS
from Utils.get_user_input import get_user_input

# Common
from Common.Web.logo_wait import wait_for_logo
from Common.Web.input_addres import input_addres
from Common.Web.person_input import (
    social_input,
    cnpj_input,
    phone_input,
    name_input
)
from Common.Web.click_next_btn import click_next_btn

# Load env
load_dotenv()
import time
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

num_accounts = int(get_user_input('Qnt ponto'))

for i in range(num_accounts):
    driver.get(os.getenv('POINT'))
    
    wait_for_logo(wait)

    name_input(driver)

    phone_input(driver)
    
    try:
        comercial = driver.find_element(
            By.XPATH, '/html/body/main/div[2]/div/form/div/div[3]/div/label[2]')
        ActionChains(driver).scroll_to_element(comercial).perform()
        comercial.click()
    except Exception as e:
        print('Error selecting the "comercial" option.\n', e)
    social_input(driver)

    cnpj_input(driver)
    
    click_next_btn(wait, driver)

    input_addres(wait, driver)

    print(i)

driver.quit()
