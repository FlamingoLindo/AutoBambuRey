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
        driver (_type_): _description_
    """
    name_input = driver.find_element(By.NAME, 'name')
    name_input.send_keys(create_random_first_name())
    
def surname_input(driver):
    """Input the person's surname

    Args:
        driver (_type_): _description_
    """
    surname_input = driver.find_element(By.NAME, 'lastName')
    surname_input.send_keys(create_random_surname())
    
def email_input(driver):
    """Input the person's email

    Args:
        driver (_type_): _description_
    """
    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys(create_random_email())
    
def cpf_input(driver):
    """Input the person's CPF

    Args:
        driver (_type_): _description_
    """
    cpf_input = driver.find_element(By.NAME, 'cpf')
    cpf_input.send_keys(create_cpf())
    
def phone_input(driver):
    """Input the person's phone

    Args:
        driver (_type_): _description_
    """
    phone_input = driver.find_element(By.NAME, 'phone')
    phone_input.send_keys(create_phone())

def social_input(driver):
    """Input the person's social name

    Args:
        driver (_type_): _description_
    """
    social_input = driver.find_element(By.NAME, 'company_name')
    social_input.send_keys(create_random_first_name())
    
def cnpj_input(driver):
    """Input the user's CNPJ

    Args:
        driver (_type_): _description_
    """
    cnpj_input = driver.find_element(By.ID, 'cnpj')
    cnpj_input.send_keys(create_cnpj())
    
def birth_input(driver):
    """Input the user's birth date

    Args:
        driver (_type_): _description_
    """
    birth_input = driver.find_element(By.NAME, 'birthdate')
    birth_input.send_keys(create_birth_day())