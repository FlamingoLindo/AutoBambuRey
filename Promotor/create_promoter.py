"""
This module is used for creating X amount of "Promotor" users.
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

# Utils
from Utils.get_user_input import get_user_input

# Common
from Common.Web.logo_wait import wait_for_logo
from Common.Web.input_addres import input_addres
from Common.Web.person_input import (
    social_input,
    cnpj_input,
    phone_input,
    name_input,
    cpf_input,
    birth_input
)
from Common.Web.send_document import input_document
from Common.Web.click_next_btn import click_next_btn

# Load env
load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

num_accounts = int(get_user_input('Qnt promotor'))

for i in range(num_accounts):
    driver.get(os.getenv('PROMOTER'))

    driver.execute_script("document.body.style.zoom = '0.4'")

    wait_for_logo(wait)

    name_input(driver)

    birth_input(driver)

    try:
        driver.switch_to.new_window('tab')
        driver.get('https://www.invertexto.com/gerador-email-temporario')
    except Exception as e:
        print('Error in opening a new.\n', e)

    try:
        copy_email = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="copiar"]')))
        copy_email.click()
    except Exception as e:
        print('Error copying the email.\n', e)
    
    try:
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print('Error switching tabs.\n', e)
    
    try:
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys(Keys.CONTROL, 'v')
    except Exception as e:
        print('Error in pasting the email.\n', e)
        
    phone_input(driver)

    cpf_input(driver)

    cnpj_input(driver)
    
    social_input(driver)

    input_document(driver)

    try:
        accept_btn = driver.find_element(
            By.XPATH, '/html/body/main/div[2]/div/form/div/div[9]/label[1]')
        accept_btn.click()
    except Exception as e:
        print('Error in accepting the terms.\n', e)

    click_next_btn(wait, driver)

    input_addres(wait, driver)

    try:
        expirience = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/main/div[2]/div/form/div/div[1]/div/label[2]')))
        expirience.click()
    except Exception as e:
        print('Error "expirience".\n', e)

    try:
        internet = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/main/div[2]/div/form/div/div[2]/div/label[2]')))
        internet.click()
    except Exception as e:
        print('Error  in "internet".\n', e)
    
    try:
        tablet = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/main/div[2]/div/form/div/div[3]/div/label[2]')))
        tablet.click()
    except Exception as e:
        print('Error in "tablet".\n', e)

    click_next_btn(wait, driver)

    try:
        driver.switch_to.window(driver.window_handles[1])
    except Exception as e:
        print('Error in switching window.\n', e)
        
    try:
        time.sleep(11)
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
    except Exception as e:
        print('Error getting the verification code.\n', e)
        
    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    try:
        code_input = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="digit1"]')))
        code_input.send_keys(code)
        code_input.submit()

        code_input = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="digit1"]')))
        code_input.send_keys(code)
        code_input.submit()
    except Exception as e:
        print('Error in sending the code.\n', e)

driver.quit()
