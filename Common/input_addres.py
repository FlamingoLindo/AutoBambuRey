"""
This module is used for inputing an addres.
"""

# Imports
import os
import time
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Load scripts
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# Utils
from Utils.addres import create_address

def input_addres(wait, driver):
    """Input addres elements

    Args:
        wait (_type_): _description_
        driver (_type_): _description_
    """
    rua, numero, cidade, cep, estado = create_address()
    
    log_input = wait.until(EC.element_to_be_clickable((By.NAME, 'street')))
    log_input.send_keys(rua)

    number_input = driver.find_element(By.NAME, 'number')
    number_input.send_keys(numero)

    neighborhood_input = driver.find_element(By.NAME, 'neighborhood')
    neighborhood_input.send_keys('Bairro')

    city_input = driver.find_element(By.NAME, 'city')
    city_input.send_keys(cidade)

    state_input = driver.find_element(By.NAME, 'uf')
    state_input.send_keys(estado)

    cep_input = wait.until(EC.element_to_be_clickable((By.NAME, 'cep')))
    cep_input.send_keys(cep)
    cep_input.submit()

    time.sleep(0.5)