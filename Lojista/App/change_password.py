"""
Change the "Lojista" user's password
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

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Common.App.lojista_login import app_lojista_login

# UTILS

capabilities = dict(
    noReset=True,
    automationName='uiautomator2',
    language='pt',
    printPageSourceOnFindFailure=True,
    appPackage='com.mestresdaweb.bambureylojistaapp',
    appActivity='com.mestresdaweb.bambureylojistaapp.MainActivity'
)

APPIUM_SERVER_URL = 'http://localhost:4723'

PASSWORD = 'Aa12345789!'

class TestAppium(unittest.TestCase):
    """
    Test case for automating the process of creating products.
    """

    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            APPIUM_SERVER_URL,
            options=UiAutomator2Options().load_capabilities(capabilities)
        )

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_change_lojista_password(self) -> None:
        """
        """        
        wait = WebDriverWait(self.driver, 10)
        
        app_lojista_login(wait, 'vitorantunes2003@gmail.com', self)
        
        menu_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Menu")')))
        menu_btn.click()
        
        profile_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Perfil')))
        profile_btn.click()
        
        change_password_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Alterar a senha')))
        change_password_btn.click()
        
        current_passw = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite sua senha atual")')))
        current_passw.send_keys('Aa12345678!')
        
        new_passw = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite sua nova senha")')
        new_passw.send_keys(PASSWORD)
        
        passw_confrim = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Confirme sua nova senha")')
        passw_confrim.send_keys(PASSWORD)
        
        for i in range(3):
            show_passw = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("com.horcrux.svg.PathView").instance({i+1})')
            show_passw.click()
            
            i += 1
        
        change_passw = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(2)')
        change_passw.click()
        
        modal_yes_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Sim, ')))
        modal_yes_opt.click()
        
        modal_sucess = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Continuar')))
        modal_sucess.click()