import time
import os
import sys
import random
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Common.App.lojista_login import app_lojista_login

from Utils.person import create_cnpj, create_random_first_name

TEST_TITLE = 'CONTA BANCÁRIA'
QA = 'Vitor FLAMINGO LINDO'
BACK = 'LUCAS LIZO'
MOBILE = 'LUCIANO ESPONJAS'
FRONT = '-'

class TestBankAccount(unittest.TestCase):

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
        app_lojista_login(wait, self)
        
    def test_02_open_bank_acc_opt(self) -> None:
        menu_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu')))
        menu_btn.click()
        
        profile_opt = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Perfil')))
        profile_opt.click()
        
        bank_opt = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Conta bancária')))
        bank_opt.click()

    def test_03_add_bank(self) -> None:
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(500, 2000)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(500, 500)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        edit_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Editar")')))
        edit_btn.click()
        
        cnpj_input = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("/")')))
        cnpj_input.clear()
        cnpj_input.send_keys(create_cnpj())
        
        digit_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(23)')
        digit_input.clear()
        digit_input.send_keys(random.randint(1,9))
        
        acc_num_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(22)')
        acc_num_input.clear()
        acc_num_input.send_keys(random.randint(1111111111,9999999999))
        
        agency_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(21)')
        agency_input.clear()
        agency_input.send_keys(random.randint(1111,9999))
        
        name_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(20)')
        name_input.clear()
        name_input.send_keys(create_random_first_name())
        
        person_type_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(19)')
        person_type_dropdown.click()
        self.driver.tap([(178, 810)])
        
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(500,500)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(500, 2000)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        
        account_type_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(18)')
        account_type_dropdown.click()
        self.driver.tap([(166, 911)])
        
        bank_type_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(17)')
        bank_type_dropdown.click()
        self.driver.tap([(360, 709)])
        
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(500, 2000)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(500, 500)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        
        save_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Salvar")')))
        save_btn.click()
        
        sucess_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Continuar')))
        sucess_modal.click()
        
        logo = wait.until(EC.visibility_of_element_located(AppiumBy.ACCESSIBILITY_ID, 'Dados da loja'))
        
        
if __name__ == '__main__':
    unittest.main()
