"""
Add X amount of cupons
"""

import time
import os
import sys
import random
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Common.App.lojista_login import app_lojista_login

from Utils.get_user_input import get_user_input

TEST_TITLE = 'CADASTRO DE CUPOM'
QA = 'Vitor Flamingo Lindo'
BACK = 'Lucas Lizo'
MOBILE = 'Luciano Esponjas'

class TestCreateCupon(unittest.TestCase):

    def setUp(self) -> None:
        capabilities = dict(
        noReset=True,
        automationName='uiautomator2',
        language='pt',
        printPageSourceOnFindFailure=True,
        appPackage='com.mestresdaweb.bambureylojistaapp',
        appActivity='com.mestresdaweb.bambureylojistaapp.MainActivity'
        )

        APPIUM_SERVER_URL = 'http://localhost:4723'

        self.driver = webdriver.Remote(
            APPIUM_SERVER_URL,
            options=UiAutomator2Options().load_capabilities(capabilities)
        )
        
        global wait
        wait = WebDriverWait(self.driver, 10)
        
    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
    
    def test_01_login(self) -> None:
        """
        Test login
        """
        app_lojista_login(wait, self)
        
    def test_02_open_cupons_page(self) -> None:
        """
        Test open "Cadastro de Cupons" page
        """
        menu_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu')))
        menu_btn.click()
        
        cupons_opt = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Cadastro de Cupons')))
        cupons_opt.click()

    def test_03_create_cupon(self) -> None:
        """
        Test create X amount of cupons
        """
        amount = 2
        for i in range(amount):
            add_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("+")')))
            add_btn.click()
        
            name_input = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o nome do cupom")')))
            name_input.send_keys(f'Auto Cupon {i+1}')
            
            add_percent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '')
            for _ in range(random.randint(1, 20)):
                add_percent.click()
        
            date_input1 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00/00/00").instance(0)')
            date_input1.send_keys('150203')
            
            date_input2 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00/00/00").instance(0)')
            date_input2.send_keys('150250')
            
            rand_min_val = random.randint(10,40)
            min_value_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("R$ 00,00")')
            min_value_input.send_keys(rand_min_val*100)
            
            rand_qnt = random.randint(10,99999)
            qnt_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("000 cupons")')
            qnt_input.send_keys(rand_qnt)
            
            categ_dropdown = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Selecione')
            categ_dropdown.click()
            self.driver.tap([(130, 2250)])
            
            close_categ_dropdown = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Todos')
            close_categ_dropdown.click()
            
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(500, 2030)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(500, 800)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(0.5)
            
            class_dropdown = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Selecione')
            class_dropdown.click()
            self.driver.tap([(150, 2147)])
            
            save_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Salvar cupom")')
            save_btn.click()
            
            sucess_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Continuar')))
            sucess_modal.click()
            
            print(f'Cupon {i+1} created\n')
 
if __name__ == '__main__':
    unittest.main()
