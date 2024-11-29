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
from Utils.person import create_random_first_name, create_cnpj, create_cpf, create_phone
from Utils.address import create_address
from Utils.mobile_gestures import take_screenshot_mobile

# Pytest metadata
TEST_TITLE = 'CRIAÇÃO DE LOJAS PROMOTOR'
QA = 'Vitor Flamingo Lindo'
BACK = 'Lucas Lizo'
MOBILE = 'Luciano Esponjas'

class TestCreateStorePromotor(unittest.TestCase):
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
               
    def test_03_open_store_page(self):
        """
        Test open "Lojas" page
        """
        store_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Lojas')))
        store_btn.click()
    
    def teste_04_add_store(self):
        """
        Test add X amount of stores
        """
        amount = 5
        for i in range(amount):
            add_store_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, ', Cadastrar loja')))
            add_store_btn.click()
            
            # Basic
            img_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, '󰏫')))
            img_btn.click()
            
            galery_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ', Abrir galeria')))
            galery_opt.click()

            album_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Álbuns')))
            album_opt.click()

            download_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Downloads")')))
            download_opt.click()         
                                                        
            image = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)')))
            image.click()
            
            name = create_random_first_name()
            social_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')))
            social_input.send_keys(name, ' Store')
            
            cnpj_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            cnpj_input.send_keys(create_cnpj())

            store_owner_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            store_owner_input.send_keys(name)
            
            cpf_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            cpf_input.send_keys(create_cpf())
            
            email_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            email_input.send_keys(name,'@gmail.com')
            
            # Swipe 1
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(455, 2052)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(475, 1210)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            
            phone_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            phone_input.send_keys(create_phone())
            
            store_email_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            store_email_input.send_keys(name,'@gmail.com')
            
            store_phone_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            store_phone_input.send_keys(create_phone())

            # address
            address = create_address()
            cep_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            cep_input.send_keys(address[3])
            
            log_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            log_input.send_keys('Banana')
            
            num_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            num_input.send_keys(address[1])
            
            comple_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            comple_input.send_keys('Complemento')
            
            # Swipe 2
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(455, 2052)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(475, 200)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(1.5)
            
            neigh_input = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')))
            neigh_input.send_keys('Bairro')

            city_input = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')))
            city_input.send_keys(address[2])
            
            time.sleep(1)
            
            uf_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...")')
            uf_input.send_keys(address[4])
            
            # Segment
            categ_dropdown = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Selecione um segmento...')
            categ_dropdown.click()
            self.driver.tap([(190, 2024)])
            
            # Register
            register_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cadastrar')
            register_btn.click()
            
            succes_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Fechar')))
            succes_modal.click()
            
            print(f'Loja {i+1} criada')
            
            pending_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pendentes')))
            pending_btn.click()
            
            store = wait.until(EC.visibility_of_any_elements_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')))
            
if __name__ == '__main__':
    unittest.main()
