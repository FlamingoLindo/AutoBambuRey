from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import sys
import re
from dotenv import load_dotenv

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# UTILS
from Utils.person import *
from Utils.addres import *
from Utils.Get_User_Input import *

load_dotenv()

upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../Images", "document.png"))

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

num_accounts = int(get_user_input('How may users'))

for i in range(num_accounts):
    driver.get(os.getenv('PROMOTER'))

    driver.execute_script("document.body.style.zoom = '0.4'")

    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gOCSyD')))

    name_input = driver.find_element(By.NAME, 'name')
    name_input.send_keys(create_random_full_name())

    birth_input = driver.find_element(By.NAME, 'birthdate')
    birth_input.send_keys(create_birth_day())

    driver.switch_to.new_window('tab')
    driver.get('https://www.invertexto.com/gerador-email-temporario')

    copy_email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="copiar"]')))
    copy_email.click()

    driver.switch_to.window(driver.window_handles[0])

    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys(Keys.CONTROL, 'v')

    phone_input = driver.find_element(By.NAME, 'phone')
    phone_input.send_keys(create_phone())

    cpf_input = driver.find_element(By.NAME, 'cpf')
    cpf_input.send_keys(create_cpf())

    cnpj_input = driver.find_element(By.ID, 'cnpj')
    cnpj_input.send_keys(create_cnpj())

    social_input = driver.find_element(By.NAME, 'company_name')
    social_input.send_keys(create_random_first_name())

    document_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    document_input.send_keys(upload_file)

    accept_btn = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/form/div/div[9]/label[1]')
    accept_btn.click()

    next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cScPww')))
    next_btn.click()

    log_input = wait.until(EC.element_to_be_clickable((By.NAME, 'street')))
    log_input.send_keys(create_address()[0])

    number_input = driver.find_element(By.NAME, 'number')
    number_input.send_keys(create_address()[1])

    neighborhood_input = driver.find_element(By.NAME, 'neighborhood')
    neighborhood_input.send_keys('Bairro')

    city_input = driver.find_element(By.NAME, 'city')
    city_input.send_keys(create_address()[2])

    state_input = driver.find_element(By.NAME, 'uf')
    state_input.send_keys(create_address()[4])

    cep_input = wait.until(EC.element_to_be_clickable((By.NAME, 'cep')))
    cep_input.send_keys(create_address()[3])
    cep_input.submit()

    expirience = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div/form/div/div[1]/div/label[2]')))
    expirience.click()

    internet = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div/form/div/div[2]/div/label[2]')))
    internet.click()

    tablet = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div/form/div/div[3]/div/label[2]')))
    tablet.click()

    next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cScPww')))
    next_btn.click()

    driver.switch_to.window(driver.window_handles[1])
    
    time.sleep(11)
    open_email = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[1]/div[3]/div[1]/table/tbody')))
    open_email.click()
    
    text_element = wait.until(EC.element_to_be_clickable((By.ID, 'body')))
    text = text_element.text

    code_match = re.search(r'\b[A-Z0-9]{6}\b', text)
    if code_match:
        code = code_match.group(0)
        print(f"The verification code is: {code}")
    else:
        print("Verification code not found.")
        
    driver.close()
        
    driver.switch_to.window(driver.window_handles[0])

    code_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="digit1"]')))
    code_input.send_keys(code)
    code_input.submit()

    code_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="digit1"]')))
    code_input.send_keys(code)
    code_input.submit()

driver.quit()