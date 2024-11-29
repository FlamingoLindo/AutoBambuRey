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

load_dotenv()

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

# Pytest metadata
TEST_TITLE = 'ALTERAÇÃO DE SENHA DO CLIENTE'
QA = 'Vitor Flamingo Lindo'
BACK = 'Lucas Lizo'
MOBILE = 'Luciano Esponjas'

class TestChangeClientPassword(unittest.TestCase):
    """
    Test the change password process for the client.
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

    def test_03_open_password_page(self) -> None:
        """
        
        """
        profile_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Perfil')))
        profile_btn.click()
        
        change_password_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alterar senha')
        change_password_btn.click()
        
    def test_04_change_password(self) -> None:
        """
        
        """
        new_password = 'Aa123456789!'
        current_password_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')))
        current_password_input.send_keys(os.getenv('CLI_PASS'))
        
        new_password_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
        new_password_input.send_keys(new_password)
        
        confirm_new_password_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(2)')
        confirm_new_password_input.send_keys(new_password)
        
        change_password = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alterar senha')
        change_password.click()
        
    def test_05_modal_message(self) -> None:
        """
        
        """
        modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Continuar')))
        assert modal.is_displayed(), "Modal message is not displayed"
        print('Password changed successfully')
        modal.click()
        
        

if __name__ == '__main__':
    unittest.main()
