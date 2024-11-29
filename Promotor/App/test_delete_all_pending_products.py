"""
Delete all pending products.
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

# Load scritps
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Utils.mobile_gestures import take_screenshot_mobile

# Pytest metadata
TEST_TITLE = 'DELETAR TODOS OS PRODUTOS EM ANÁLISE PROMOTOR'
QA = 'Vitor Flamingo Lindo'
BACK = 'Lucas Lizo'
MOBILE = 'Luciano Esponjas'
TYPE = 'Promotor'

class TestDelteAllPendingProductstPromotor(unittest.TestCase):
    """
    Test case for automating the process of creating products.
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
        
        
    def test_03_open_store(self):
        """
        Test open "Lojas" page
        """
        stores_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Lojas')))
        assert stores_btn.is_displayed(), 'Botão "Lojas" não encontrado'
        stores_btn.click()
        
        select_store = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Flamingo")')))
        select_store.click()
        
        time.sleep(1)
        
        pending_tab = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Pendentes')))
        pending_tab.click()
        
    def test_04_delete(self):
        """
        Test delete all pending products
        """
        try:
            trash_icon = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(0)')))
            
            while trash_icon.is_displayed():
                trash_icon.click()
                
                published_tab = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Publicados')))
                published_tab.click()
                
                pending_tab = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Pendentes')))
                pending_tab.click()
                
                trash_icon = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(0)')))
            
            print('No more products!')
        
        except Exception as e:
            print('No more trash icons or encountered an error:', e)

if __name__ == '__main__':
    unittest.main()
