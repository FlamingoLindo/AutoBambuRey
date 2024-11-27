import os
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

def app_lojista_login(wait, self):

    email_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Digite seu e-mail")')))
    email_input.send_keys(os.getenv('LOJ_EMAIL'))

    password = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite sua senha aqui")')
    password.send_keys(os.getenv('LOJ_PASS'))

    login_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Entrar")')
    login_btn.click()
    
    try:
        # Wait for the error message if it appears
        error_msg = wait.until(EC.visibility_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("E-mail obrigatório")')
        ))
        # If the error message appears, assert failure
        assert False, error_msg.text == 'E-mail obrigatório'; f"Unexpected error message: {error_msg.text}"
    except TimeoutException:
        # No error message, login is successful
        print('E-mail e senha corretos')
        print('Login realizado com sucesso!')
    