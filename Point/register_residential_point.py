from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import sys
from dotenv import load_dotenv

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# UTILS
from Utils.person import *
from Utils.addres import *

load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get(os.getenv('POINT'))

logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gOCSyD')))

name = driver.find_element(By.NAME, 'name')
name.send_keys(create_random_full_name())

phone = driver.find_element(By.NAME, 'phone')
phone.send_keys(create_phone())

residential = driver.find_element(By.CSS_SELECTOR, '.eEcEoS')
residential.click()

cpf = driver.find_element(By.NAME, 'cpf')
cpf.send_keys(create_cpf())
cpf.submit()

log_input = driver.find_element(By.NAME, 'street')
log_input.send_keys(create_address()[0])

number_input = driver.find_element(By.NAME, 'number')
number_input.send_keys(create_address()[1])

neighborhood_input = driver.find_element(By.NAME, 'neighborhood')
neighborhood_input.send_keys('Bairro')

city_input = driver.find_element(By.NAME, 'city')
city_input.send_keys(create_address()[2])

state_input = driver.find_element(By.NAME, 'uf')
state_input.send_keys(create_address()[4])

cep_input = wait.until(EC.element_to_be_clickable((By.ID, 'cep')))
cep_input.send_keys(create_address()[3])

time.sleep(10)
driver.quit()