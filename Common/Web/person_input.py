"""
This module is used for inputing a person informations.
"""

# Imports
import os
import sys
from selenium.webdriver.common.by import By

# Load scripts
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# UTILS
from Utils.person import (
    create_random_email,
    create_random_first_name,
    create_random_surname,
    create_cpf,
    create_phone,
    create_cnpj,
    create_birth_day
)

def name_input(driver):
    """Input the person's name

    Args:
        driver (WebDriver): Selenium WebDriver instance used 
        for interacting with the browser.
    """
    try:
        name_input = driver.find_element(By.NAME, 'name')
        name_input.send_keys(create_random_first_name())
    except Exception as e:
        print('Error in "name".\n', e)
        
        
def surname_input(driver):
    """Input the person's surname

    Args:
        driver (_type_): _description_
    """
    try:
        surname_input = driver.find_element(By.NAME, 'lastName')
        surname_input.send_keys(create_random_surname())
    except Exception as e:
        print('Error in "surname".\n', e)
        
        
def email_input(driver):
    """Input the person's email

    Args:
        driver (_type_): _description_
    """
    try:
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys(create_random_email())
    except Exception as e:
        print('Error in "email".\n', e)
        
    
def cpf_input(driver):
    """Input the person's CPF

    Args:
        driver (_type_): _description_
    """
    try:
        cpf_input = driver.find_element(By.NAME, 'cpf')
        cpf_input.send_keys(create_cpf())
    except Exception as e:
        print('Error in "CPF".\n', e)
        
    
def phone_input(driver):
    """Input the person's phone

    Args:
        driver (_type_): _description_
    """
    try:
        phone_input = driver.find_element(By.NAME, 'phone')
        phone_input.send_keys(create_phone())
    except Exception as e:
        print('Error in "telefone".\n', e)
        
        
def social_input(driver):
    """Input the person's social name

    Args:
        driver (_type_): _description_
    """
    try:
        social_input = driver.find_element(By.NAME, 'company_name')
        social_input.send_keys(create_random_first_name())
    except Exception as e:
        print('Error in "razão social".\n', e)
        
    
def cnpj_input(driver):
    """Input the user's CNPJ

    Args:
        driver (_type_): _description_
    """
    try:
        cnpj_input = driver.find_element(By.ID, 'cnpj')
        cnpj_input.send_keys(create_cnpj())
    except Exception as e:
        print('Error in "CNPJ".\n', e)
        
    
def birth_input(driver):
    """Input the user's birth date

    Args:
        driver (_type_): _description_
    """
    try:
        birth_input = driver.find_element(By.NAME, 'birthdate')
        birth_input.send_keys(create_birth_day())
    except Exception as e:
        print('Error in "data de nascimento".\n', e)
        