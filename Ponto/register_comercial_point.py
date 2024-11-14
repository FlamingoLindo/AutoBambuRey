"""
This module is used for creating X amount of "Pontos comerciais".
"""

# Imports
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Import env
from dotenv import load_dotenv

# Load scripts
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# UTILS
from Utils.get_user_input import get_user_input

# Common
from Common.logo_wait import wait_for_logo
from Common.input_addres import input_addres
from Common.person_input import (
    social_input,
    cnpj_input,
    phone_input,
    name_input
)
from Common.click_next_btn import click_next_btn

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

    comercial = driver.find_element(
        By.XPATH, '/html/body/main/div[2]/div/form/div/div[3]/div/label[2]')
    comercial.click()

    social_input(driver)

    cnpj_input(driver)
    
    click_next_btn(wait, driver)

    input_addres(wait, driver)

    print(i)

driver.quit()
