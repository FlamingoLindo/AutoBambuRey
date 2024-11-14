"""
This module is used for inputing in to the password and password confirmation inputs.
"""

# Imports
import os
import sys
from selenium.webdriver.common.by import By

# Load scripts
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

PASSWORD = 12345678

def password_input(wait, driver):
    """Input password and password confirmation

    Args:
        wait (_type_): _description_
        driver (_type_): _description_
    """
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(PASSWORD)

    confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
    confirm_password_input.send_keys(PASSWORD)
    confirm_password_input.submit()