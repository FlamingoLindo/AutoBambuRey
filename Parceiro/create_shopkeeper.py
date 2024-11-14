"""
This module is used for creating X amount of "Parceiros" users.
"""

# Imports
import os
import time
import sys
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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
    name_input,
    cpf_input,
)
from Common.send_document import input_document
from Common.click_next_btn import click_next_btn

load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

num_accounts = int(get_user_input('Qnt parceiros'))

for i in range(num_accounts):
    driver.get(os.getenv('SHOPKEEPER'))

    driver.execute_script("document.body.style.zoom = '0.4'")

    wait_for_logo(wait)

    social_input(driver)

    cnpj_input(driver)

    driver.switch_to.new_window('tab')
    driver.get('https://www.invertexto.com/gerador-email-temporario')

    copy_email = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="copiar"]')))
    copy_email.click()

    driver.switch_to.window(driver.window_handles[0])

    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys(Keys.CONTROL, 'v')

    phone_input(driver)

    name_input(driver)

    cpf_input(driver)

    input_document(driver)

    accept_btn = driver.find_element(
        By.XPATH, '/html/body/main/div[2]/div[2]/form/div/div[8]/label[1]')
    accept_btn.click()

    click_next_btn(wait, driver)

    input_addres(wait, driver)
    
    segment_dropdown = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/main/div[2]/div/form/div/div/div/div/div[1]')))
    segment_dropdown.click()

    acessories_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="react-select-segment-option-0"]')))
    acessories_option.click()

    click_next_btn(wait, driver)

    driver.switch_to.window(driver.window_handles[1])

    time.sleep(6.4)
    open_email = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/main/div[1]/div[3]/div[1]/table/tbody')))
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

    code_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="digit1"]')))
    code_input.send_keys(code)
    code_input.submit()

    print(i)

driver.quit()
