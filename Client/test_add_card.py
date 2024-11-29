import time
import os
import sys
import os
from dotenv import load_dotenv
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

from Utils.card import create_card
from Utils.person import create_random_full_name, create_cpf
from Utils.mobile_gestures import take_screenshot_mobile
load_dotenv()

# Pytest metadata
TEST_TITLE = 'CADASTRO DE CARTÃO DE CRÉDITO CLIENTE'
QA = 'Vitor Flamingo Lindo'
BACK = 'Lucas Lizo'
MOBILE = 'Luciano Esponjas'
TYPE = 'Cliente'

class TestAddClientCard(unittest.TestCase):
    """
    Test the add card process for the client.
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
        menu_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Menu')))
        assert menu_btn.is_displayed(), "Menu button is not visible"
        print('Menu opened successfully')
        screenshotBase64 = self.driver.get_screenshot_as_base64()

    def test_02_login(self) -> None:
        """
        Test the login process.
        """
        profile_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Perfil')))
        profile_btn.click()

        login_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Entrar')))
        login_btn.click()

        email = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite seu e-mail")')))
        email.send_keys(os.getenv('CLI_EMAIL'))

        password = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite sua senha")')))
        password.send_keys(os.getenv('CLI_PASS'))

        log_in = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Entrar")')
        log_in.click()
        print('Logged in successfully')

    def test_03_open_card_page(self) -> None:
        """
        
        """
        profile_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Perfil')))
        profile_btn.click()
        
        card_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cartões cadastrados')
        card_btn.click()
        
    def test_04_add_card(self) -> None:
        """
        
        """
        amount = 2
        for i in range(amount):
            add_card_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Adicionar cartão')))
            add_card_btn.click()
            
            card = create_card()
            card_num_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
            card_num_input.send_keys(card[2])
            
            card_exp_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
            card_exp_input.send_keys(card[3])
            
            cvv_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(2)')
            cvv_input.send_keys(card[4])
            
            name_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(3)')
            name_input.send_keys(create_random_full_name())
            
            cpf_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(4)')
            cpf_input.send_keys(create_cpf())
            
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Adicionar')
            add_btn.click()
            
            try:
                error_msm = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("toastContentContainer")')))
                if error_msm.is_displayed():
                    take_screenshot_mobile(self)
                    assert False, f'Erro ao Gerar Token do Cartão'
            except Exception as e:
                raise AssertionError("An error occurred while adding the card") from e

if __name__ == '__main__':
    unittest.main()
