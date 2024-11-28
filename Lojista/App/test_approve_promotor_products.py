"""
Approve all "Promotor" products.
"""

# Imports
import os
import sys
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Load scripts
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

# Scripts
from Common.App.lojista_login import app_lojista_login

# Pytest metadata
TEST_TITLE = 'APROVAR PRODUTOS DE PROMOTORES'
QA = 'Vitor Flamingo Lindo'
BACK = 'Lucas Lizo'
MOBILE = 'Luciano Esponjas'

class TestApprovePromotorProducts(unittest.TestCase):

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
        
    def test_02_open_promotor_page(self) -> None:
        """
        Test open "Promotor" page
        """
        promotor_page = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Promotor')))
        promotor_page.click()
        
    def test_03_approve_products(self) -> None:
        """
        Test approve all products
        """
        try:
            approve_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
            
            while approve_btn.is_displayed():
                approve_btn.click()
                
                sucess_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Continuar')))
                sucess_modal.click()
                
                approve_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
            print('No more products')
        except:
            pass
 
if __name__ == '__main__':
    unittest.main()
