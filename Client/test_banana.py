"""
Teste de check-in do cliente.
"""
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

from Utils.mobile_gestures import app_swipe

load_dotenv()

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# Pytest metadata
TEST_TITLE = 'REALIZAR CHECK-IN'
QA = 'Vitor Flamingo Lindo'
BACK = 'Lucas Lizo'
MOBILE = 'Luciano Esponjas'
TYPE = 'Cliente'

class banana(unittest.TestCase):
    """
    Teste de check-in do cliente.
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

    def test_03_open_check_in_page(self) -> None:
        """
        Test open check-in page.
        """
        profile_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Perfil')))
        profile_btn.click()

        app_swipe(self, 500, 1000, 500, 500)
        
        pref_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Minhas preferências')))
        pref_btn.click()
        
    def test_04_get_len(self) -> None:
        modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Do que você mais gosta?, Escolha as categorias da sua preferência (opcional)')))
        
        categs = self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView")')
        
        print('HDJAHDKJAHKDHADJKH ', len(categs))
        
if __name__ == '__main__':
    unittest.main()
