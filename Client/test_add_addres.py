import time
import os
import sys
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

from Utils.address import create_address
from Utils.mobile_gestures import app_swipe
from Utils.mobile_gestures import take_screenshot_mobile

# Pytest metadata
TEST_TITLE = 'CRIAÇÃO DE LOJAS PROMOTOR'
QA = 'Vitor Flamingo Lindo'
BACK = 'Lucas Lizo'
MOBILE = 'Luciano Esponjas'
TYPE = 'Cliente'

class TestAddaddressClient(unittest.TestCase):
    """
    
    """

    def setUp(self) -> None:
        capabilities = dict(
            noReset=True,
            automationName='uiautomator2',
            language='pt',
            printPageSourceOnFindFailure=True,
            appPackage='com.mestresdaweb.bamburey',
            appActivity='com.mestresdaweb.bamburey.MainActivity'
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

    def test_01_open_app(self) -> None:
        """
        Test that the menu button is visible and clickable.
        """
        time.sleep(6)
        
        menu_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Menu')))
        assert menu_btn.is_displayed(), "Menu button is not visible"
        print('Menu opened successfully')

    def test_02_login(self) -> None:
        """
        Test the login process.
        """
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
        print('Logged in successfully')

    def test_03_open_address_page(self) -> None:
        """
        
        """
        profile_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Perfil')))
        profile_btn.click()
        
        address_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Meus endereços')))
        address_btn.click()
        
    def test_04_add_address(self) -> None:
        """
        
        """
        amount = 50
        for i in range (amount):
            try:
                add_btn = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("Adicionar endereço"))')))
            except:
                take_screenshot_mobile(self)
                assert False, 'Could not find register address button'
            time.sleep(0.5)
            add_btn.click()
            
            address = create_address()
            cep_input = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: 12345-678")')))
            cep_input.send_keys(address[3])
            
            state_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: São Paulo").instance(0)')
            state_input.send_keys(address[4])
            
            city_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: São Paulo")')
            city_input.send_keys(address[2])
            
            neighborhood_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: Jardim Paulista")')
            neighborhood_input.send_keys('Bairro')
            
            log_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: rua, avenida, praça...")')
            log_input.send_keys('Logradouro')
            
            number_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ex: 100")')
            number_input.send_keys(address[1])
            
            app_swipe(self, 500, 2000, 500, 500)
            
            save_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Salvar endereço')
            save_btn.click()
            
            time.sleep(0.5)
            
            print(f'Endereço {i+1} cadastrado')
            
        
        

if __name__ == '__main__':
    unittest.main()
