"""
This module is used for creating X amount of "Influenciadores" users.
"""

# Imports
import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Import env
from dotenv import load_dotenv

# Load scripts
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# Utils
from Utils.get_user_input import get_user_input

# Common
from Common.logo_wait import wait_for_logo
from Common.click_next_btn import click_next_btn
from Common.person_input import (
    name_input,
    email_input,
    phone_input
)

# Load env
load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

num_accounts = int(get_user_input('Qnt influenciadores'))

for i in range(num_accounts):
    driver.get(os.getenv('INFLUENCER'))

    wait_for_logo(wait)

    name_input(driver)

    email_input(driver)

    phone_input(driver)

    click_next_btn(wait, driver)

    try:
        facebook_input = wait.until(EC.element_to_be_clickable((By.NAME, 'facebook')))
        facebook_input.send_keys('https://www.facebook.com/mestresdaweboficial/')
    except Exception as e:
        print('Error in "facebook".\n', e)

    try:
        instagram_input = driver.find_element(By.NAME, 'instagram')
        instagram_input.send_keys('https://www.instagram.com/mestresdaweb/')
    except Exception as e:
        print('Error in "instagram".\n', e)
    
    try:
        tiktok_input = driver.find_element(By.NAME, 'tiktok')
        tiktok_input.send_keys('https://www.tiktok.com/@mestresdaweb')
    except Exception as e:
        print('Error in "tik tok".\n', e)
        
    try:
        youtube_input = driver.find_element(By.NAME, 'youtube')
        youtube_input.send_keys('https://www.youtube.com/channel/UC64RO26j3E4bJmkjnRGJ4Kg')
        youtube_input.submit()
    except Exception as e:
        print('Error in "youtube".\n', e)
        
    time.sleep(0.5)

    print(i)

driver.quit()