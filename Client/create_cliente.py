"""
This module is used for creating X amount of "Clientes" users.
"""

import time
import os
import sys
import re
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

from Utils.get_user_input import get_user_input
from Utils.person import (
    create_random_full_name,
    create_phone,
    create_birth_day
)

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

PASSWORD = 'Aa12345678!'

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

    def test_create_app_user(self) -> None:
        """
        Test the user registration process by automating the input of user details 
        and verifying the actions required for successful account creation.

        The method simulates the user actions of filling in a form, clicking buttons, 
        copying an email, and interacting with various app screens.
        """

        wait = WebDriverWait(self.driver, 10)

        time.sleep(6)

        # home
        wait.until(EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, 'Menu'))
        )

        profile_btn = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, 'Perfil'))
        )
        profile_btn.click()

        login_btn = wait.until(EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, 'Entrar'))
        )
        login_btn.click()

        num_accounts = int(get_user_input('How may users'))
        for i in range(num_accounts):
            # logo
            wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
                )
            )

            register_btn = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("Faça seu cadastro aqui")')
            ))
            register_btn.click()

            name_input = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().text("Digite seu nome completo")')
                )
            )
            name_input.send_keys(create_random_full_name())

            phone_input = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("Digite seu telefone")')
            ))
            phone_input.send_keys(create_phone())

            birth_input = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("DD/MM/AAAA")')
            ))
            birth_input.send_keys(create_birth_day())

            next_btn = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("android.view.View").instance(2)')
            ))
            next_btn.click()

            self.driver.press_keycode(AndroidKey.HOME)

            google_icon = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Free Adblocker Browser'))
            )
            google_icon.click()

            time.sleep(1)

            search_bar = self.driver.find_element(
                AppiumBy.ID, 'com.hsv.freeadblockerbrowser:id/url_bar')
            search_bar.click()
            time.sleep(0.5)
            search_bar2 = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Gerador de Email Temporário | invertexto.com")'
            )
            search_bar2.click()

            time.sleep(4)

            copy = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("copiar")')
            copy.click()

            self.driver.press_keycode(AndroidKey.APP_SWITCH)
            time.sleep(0.5)
            self.driver.press_keycode(AndroidKey.APP_SWITCH)

            email_input = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("Digite seu e-mail")')
            ))
            email_input.send_keys(self.driver.get_clipboard_text())

            password_input = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("Digite sua senha")')
            ))
            password_input.send_keys(PASSWORD)

            password_conf_input = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("Confirme sua senha")')
            ))
            password_conf_input.send_keys(PASSWORD)

            accept_terms = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("android.view.ViewGroup").instance(21)')
            ))
            accept_terms.click()

            next_btn = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("android.view.View").instance(2)')
            ))
            next_btn.click()

            self.driver.press_keycode(AndroidKey.APP_SWITCH)
            time.sleep(0.5)
            self.driver.press_keycode(AndroidKey.APP_SWITCH)

            self.driver.swipe(start_x=500, start_y=1950,
                              end_x=500, end_y=1845, duration=100)

            time.sleep(4.1)

            open_email = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("Codigo de verificação")')
            ))
            open_email.click()

            time.sleep(1)

            code_text = wait.until(EC.visibility_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().textContains("o código de verificação é")')
            ))

            text = code_text.text.strip()
            print(f"Extracted Text: '{text}'")

            code_match = re.search(r'\b[A-Z0-9]{6}\b', text)
            if code_match:
                code = code_match.group(0)
                print(f"The verification code is: {code}")
            else:
                print("Verification code not found.")

            self.driver.swipe(start_x=500, start_y=300,
                              end_x=500, end_y=1900, duration=100)

            self.driver.press_keycode(AndroidKey.APP_SWITCH)
            time.sleep(0.5)
            self.driver.press_keycode(AndroidKey.APP_SWITCH)

            time.sleep(1)

            code_input = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText")'
            )
            code_input.send_keys(code)

            next_btn = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(2)'
            )
            next_btn.click()

            time.sleep(2)

            # check_icon
            wait.until(EC.visibility_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("android.view.ViewGroup").instance(4)')
            ))

            login_btn2 = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, 'Ir para login')
            login_btn2.click()

            time.sleep(0.5)
            print(i)


if __name__ == '__main__':
    unittest.main()
