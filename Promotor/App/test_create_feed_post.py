"""
Create a X amount of feed posts by the "Promotor" user.
"""

# Imports
import os
import sys
import random
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

# Load scripts
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Utils.mobile_gestures import take_screenshot_mobile

# Pytest metadata
TEST_TITLE = 'CRIAÇÃO DE PRODUTO PROMOTOR'
QA = 'VITOR FLAMINGO LINDO'
BACK = 'LUCAS LIZO'
MOBILE = 'LUCIANO ESPONJAS'

class TestCreateFeedPostPromotor(unittest.TestCase):
    """
    Test case for automating the process of creating feed posts.
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
               
    def test_03_open_feed_page(self):
        """
        Test open "Feed" page
        """
        feed_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Feed')))
        feed_btn.click()
    
    def teste_04_create_post(self):
        """
        Test create a X amount of feed posts
        """
        amount = 2
        for i in range(amount):
            
            add_post_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, ', Adicionar')))
            add_post_btn.click()

            store_dropdown = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Selecione a loja que deseja')))
            store_dropdown.click()
            self.driver.tap([(182, 626)])
            
            loop_count = random.randint(2, 3)

            for img_loop in range(loop_count):
                add_image_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(5)')))
                add_image_btn.click()
                
                galery_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ', Abrir galeria')))
                galery_opt.click()

                album_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Álbuns')))
                album_opt.click()

                download_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Downloads")')))
                download_opt.click()         
                                                            
                image = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance({img_loop+1})')))
                image.click()

                img_loop += 1
            
            desc_input = self.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText')
            desc_input.send_keys(f'Auto Feed Post {i+1}')
            
            link_prod = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Vincular ao produto, ')
            link_prod.click()
            
            see_prod_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Ver, ')))
            see_prod_btn.click()
            
            bind_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Vincular')))
            bind_btn.click()
            
            publish_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Publicar')))
            publish_btn.click()
        
            sucess_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Fechar')))
            sucess_modal.click()
        
if __name__ == '__main__':
    unittest.main()
