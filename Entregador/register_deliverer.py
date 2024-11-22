"""
This module is used for creating X amount of "Entregador" users.
"""

# Imports
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
from Common.Web.password_input import password_input
from Common.Web.person_input import (
    name_input,
    surname_input,
    email_input,
    cpf_input
)

# Load env
load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

num_accounts = int(get_user_input('Qnt entregadores?'))

for i in range(num_accounts):
    driver.get(os.getenv('DELIVERER'))

    wait_for_logo(wait)

    name_input(driver)

    surname_input(driver)

    email_input(driver)

    cpf_input(driver)

    password_input(wait, driver)
    
    input_addres(wait, driver)
    
    print(i)

driver.quit()
