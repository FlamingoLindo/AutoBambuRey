"""

"""

import time
import os
import sys
import re
import random
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

from Common.App.login import app_login

# UTILS

capabilities = dict(
    noReset=False,
    automationName='uiautomator2',
    language='pt',
    printPageSourceOnFindFailure=True,
    appPackage='com.mestresdaweb.bamburey',
    appActivity='com.mestresdaweb.bamburey.MainActivity'
)

APPIUM_SERVER_URL = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    """
    Test case for automating the process of creating users and 
    testing the app's registration process.

    This class uses Appium to interact with the mobile application, 
    automates the registration process for
    multiple users, and handles actions such as entering data, 
    verifying emails, and handling app navigation.
    """

    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            APPIUM_SERVER_URL,
            options=UiAutomator2Options().load_capabilities(capabilities)
        )

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_buy_product(self) -> None:
        """
        
        """
        
        wait = WebDriverWait(self.driver, 10)
        
        time.sleep(6)
        
        wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Menu')))
        
        profile_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Perfil')))
        profile_btn.click()

        login_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Entrar')))
        login_btn.click()
        
        email = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite seu e-mail")')))
        email.send_keys('flamingolindo1@gmail.com')
        
        password = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite sua senha")')))
        password.send_keys('Aa12345678!')
        
        log_in = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Entrar")')
        log_in.click()
        
        search_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pesquisar por nome/id do produto')))
        search_btn.click()
        
        search_input = wait.until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.EditText')))
        search_input.send_keys('Automático')
        
        click_product = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Batom automático 1")')))
        click_product.click()
        
        add_cart_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Adicionar ao carrinho')))
        add_cart_btn.click()
        
        cart_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continuar")')))
        cart_modal.click()
        
        add_all_items = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Tudo")')))
        add_all_items.click()
        
        close_cart_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Finalizar compra')
        close_cart_btn.click()
        
        continue_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continuar")')))
        continue_btn.click()
        
        payment_opt_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Método de pagamento, ')))
        payment_opt_btn.click()
        
        pix_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pix')))
        pix_opt.click()
        
        review_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Revisar pedido')))
        review_btn.click()
        
        self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=900, duration=800)
        time.sleep(1.2)
        confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Confirmar compra')
        confirm_btn.click()
        
        time.sleep(2)
        
        self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=900, duration=800)
        
        time.sleep(0.5)
        
        ok_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Ok')))
        ok_btn.click()
        
        sucess_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Continuar')))
        sucess_modal.click()
        
        menu_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Menu")')))
        menu_btn.click()
        
        my_purchases = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Meus Pedidos')))
        my_purchases.click()
        
        purchase = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aguardando pagamento").instance(0)')))
        
        time.sleep(5)
        
        
        
if __name__ == '__main__':
    unittest.main()
