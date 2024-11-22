from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

def app_lojista_login(wait, email, self):
    
    try:
        email_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite seu e-mail aqui")')))
        email_input.send_keys(email)
    except Exception as e:
        print('An error occured in the e-mail input.\n', e)
    
    try:
        password = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite sua senha aqui")')
        password.send_keys('12345678')
    except Exception as e:
        print('An error occured in the password input.\n', e)
        
    try:
        login_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Entrar")')
        login_btn.click()
    except Exception as e:
        print('An error occured when clicking in the login button.\n', e)
        
    print('Login realizado com sucesso!')
    