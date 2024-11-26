import os
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

def app_lojista_login(wait, self):

    email_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite seu e-mail aqui")')))
    email_input.send_keys(os.getenv('LOJ_EMAIL'))

    password = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite sua senha aqui")')
    password.send_keys(os.getenv('LOJ_PASS'))

    login_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Entrar")')
    login_btn.click()
    
    try:
        error_msg = 
        assert False, 'Error in login'
    except:
        pass
 
    print('Login realizado com sucesso!')
    