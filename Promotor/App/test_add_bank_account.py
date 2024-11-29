"""
Create a X amount of stores by the "Promotor" user.
"""

# Imports
import time
import os
import sys
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Load scripts
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

# Import scripts
from Utils.mobile_gestures import take_screenshot_mobile, app_tap, app_swipe
from Utils.person import create_random_full_name, create_cpf
from Utils.card import create_bank_account

# Pytest metadata
TEST_TITLE = 'ADICIONAR CONTA BANCÁRIA'
QA = 'Vitor Flamingo Lindo'
BACK = 'Lucas Lizo'
MOBILE = 'Luciano Esponjas'

class TestAddbankAccountPromotor(unittest.TestCase):
    """
    Test case for automating the process of creating stores.
    """
    
    def setUp(self) -> None:
        capabilities = dict(
        noReset=True,
        automationName='uiautomator2',
        language='pt',
        printPageSourceOnFindFailure=True,
        appPackage='com.mestresdaweb.bambureypromotor',
        appActivity='com.mestresdaweb.bambureypromotor.MainActivity'
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
        email_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Digite seu e-mail")')))
        email_input.send_keys(os.getenv('PRO_EMAIL'))

        password = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Digite sua senha")')
        password.send_keys(os.getenv('PRO_PASS'))

        login_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Entrar")')
        login_btn.click()
        
        try:
            # Wait for the error message if it appears
            error_msg = wait.until(EC.visibility_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Email Inválido")')
            ))
            # If the error message appears, assert failure
            take_screenshot_mobile(self)
            assert False, error_msg.text == 'Email Inválido'; f"Unexpected error message: {error_msg.text}"
        except TimeoutException:
            # No error message, login is successful
            print('E-mail e senha corretos')
            print('Login realizado com sucesso!')
        
    def test_02_close_bank(self):
        """
        Test close bank modal
        """
        bank_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ir")')))
        assert bank_modal.is_displayed(), 'Promotor tem conta bancária'
        bank_modal.click() 
        
        go_back_arrow = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')))
        assert go_back_arrow.is_displayed(), 'Botão de "Voltar" não encontrado'
        go_back_arrow.click()
               
    def test_03_open_bank_page(self):
        """
        
        """
        config_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Configurações')))
        config_btn.click()
        
        bank_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Conta bancária')))
        bank_btn.click()
        
    def test_04_add_bank_account(self):
        """
        
        """
        bank_dropdown = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'ex: Bradesco')))
        bank_dropdown.click()
        app_tap(self, 500, 780)
        
        account_type_dropdown = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'ex: Conta Corrente')
        account_type_dropdown.click()
        app_tap(self, 246, 891)
        
        person_type_dropdown = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'ex: Jurídica')
        person_type_dropdown.click()
        app_tap(self, 198, 1164)
        
        name_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: José Maria da Silva")')
        name_input.send_keys(create_random_full_name())
        
        bank = create_bank_account()
        agency_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: 0000"))')
        agency_input.send_keys(bank[0])
        
        account_num_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: 0000000")')
        account_num_input.send_keys(bank[1])
        
        digit_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: 0")')
        digit_input.send_keys(bank[2])
        
        app_swipe(self, 500, 1500, 500, 500)
        
        cpf_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: 000.000.000-00")')
        cpf_input.send_keys(create_cpf())
        
        register_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cadastrar')
        register_btn.click()
        
        
        
                  
if __name__ == '__main__':
    unittest.main()
