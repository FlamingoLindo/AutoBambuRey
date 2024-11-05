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
from Utils.Get_User_Input import *

load_dotenv()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

num_accounts = int(get_user_input('How may users'))

for i in range(num_accounts):
    driver.get(os.getenv('INFLUENCER'))

    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gOCSyD')))

    name_input = driver.find_element(By.NAME, 'name')
    name_input.send_keys(create_random_full_name())

    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys(create_random_email())

    phone_input = driver.find_element(By.NAME, 'phone')
    phone_input.send_keys(create_phone())
    phone_input.submit()

    facebook_input = wait.until(EC.element_to_be_clickable((By.NAME, 'facebook')))
    facebook_input.send_keys('https://www.facebook.com/mestresdaweboficial/')

    instagram_input = driver.find_element(By.NAME, 'instagram')
    instagram_input.send_keys('https://www.instagram.com/mestresdaweb/')

    tiktok_input = driver.find_element(By.NAME, 'tiktok')
    tiktok_input.send_keys('https://www.tiktok.com/@mestresdaweb')

    youtube_input = driver.find_element(By.NAME, 'youtube')
    youtube_input.send_keys('https://www.youtube.com/channel/UC64RO26j3E4bJmkjnRGJ4Kg')

driver.quit()