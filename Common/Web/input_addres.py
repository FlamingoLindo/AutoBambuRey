"""
This module is used for inputing an address.
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
from Utils.address import create_address

def input_address(wait, driver):
    """Input address elements

    Args:
        wait (WebDriverWait): Selenium WebDriverWait instance used 
        for waiting for elements to be in a certain state.
        
        driver (WebDriver): Selenium WebDriver instance used 
        for interacting with the browser.
    """
    rua, numero, cidade, cep, estado = create_address()
    
    try:
        log_input = wait.until(EC.element_to_be_clickable((By.NAME, 'street')))
        log_input.send_keys(rua)
    except Exception as e:
        print('Error in "logradouro".\n', e)

    try:
        number_input = driver.find_element(By.NAME, 'number')
        number_input.send_keys(numero)
    except Exception as e:
        print('Error in "número".\n', e)
    
    try:
        neighborhood_input = driver.find_element(By.NAME, 'neighborhood')
        neighborhood_input.send_keys('Bairro')
    except Exception as e:
        print('Error in "bairro".\n', e)

    try:
        city_input = driver.find_element(By.NAME, 'city')
        city_input.send_keys(cidade)
    except Exception as e:
        print('Error in "cidade".\n', e)
    
    try:
        state_input = driver.find_element(By.NAME, 'uf')
        state_input.send_keys(estado)
    except Exception as e:
        print('Error in "estado".\n', e)

    try:
        cep_input = wait.until(EC.element_to_be_clickable((By.NAME, 'cep')))
        cep_input.send_keys(cep)
        cep_input.submit()
    except Exception as e:
        print('Error in "CEP".\n', e)

    time.sleep(0.5)