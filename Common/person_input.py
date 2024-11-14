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
    name_input = driver.find_element(By.NAME, 'name')
    name_input.send_keys(create_random_first_name())
    
def surname_input(driver):
    surname_input = driver.find_element(By.NAME, 'lastName')
    surname_input.send_keys(create_random_surname())
    
def email_input(driver):
    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys(create_random_email())
    
def cpf_input(driver):
    cpf_input = driver.find_element(By.NAME, 'cpf')
    cpf_input.send_keys(create_cpf())
    
def phone_input(driver):
    phone_input = driver.find_element(By.NAME, 'phone')
    phone_input.send_keys(create_phone())

def social_input(driver):
    social_input = driver.find_element(By.NAME, 'company_name')
    social_input.send_keys(create_random_first_name())
    
def cnpj_input(driver):
    cnpj_input = driver.find_element(By.ID, 'cnpj')
    cnpj_input.send_keys(create_cnpj())
    
def birth_input(driver):
    birth_input = driver.find_element(By.NAME, 'birthdate')
    birth_input.send_keys(create_birth_day())