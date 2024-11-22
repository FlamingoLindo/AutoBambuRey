"""

"""

import time
import os
import sys
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

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

    def test_buy_product(self) -> None:
        """
        Test buying a product in the app.
        """
        wait = WebDriverWait(self.driver, 10)
        time.sleep(6)

        try:
            menu_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Menu')))
            print('Menu encontrado')
        except Exception as e:
            print('Error waiting for "Menu" to appear:', e)
        
        try:
            profile_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Perfil')))
            profile_btn.click()
            print('Botão de perfil encontrado')
        except Exception as e:
            print('Error clicking on "Perfil":', e)
        
        try:
            login_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Entrar')))
            login_btn.click()
            print('Botão de login encontrado')
        except Exception as e:
            print('Error clicking on "Entrar":', e)

        try:
            email = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite seu e-mail")')))
            email.send_keys('flamingolindo1@gmail.com')
            print('E-mail adicionado')
        except Exception as e:
            print('Error entering email:', e)

        try:
            password = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite sua senha")')))
            password.send_keys('Aa12345678!')
            print('Senha adicionada')
        except Exception as e:
            print('Error entering password:', e)

        try:
            log_in = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Entrar")')
            log_in.click()
            print('Botão de login encontrado')
        except Exception as e:
            print('Error clicking on "Entrar" button:', e)

        try:
            search_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pesquisar por nome/id do produto')))
            search_btn.click()
            print('Busca encontrada')
        except Exception as e:
            print('Error clicking on search button:', e)

        try:
            search_input = wait.until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.EditText')))
            search_input.send_keys('Automático')
            print('Nome do produto enviado')
        except Exception as e:
            print('Error entering product name:', e)

        try:
            click_product = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Batom automático 1")')))
            click_product.click()
            print('Produto clicado')
        except Exception as e:
            print('Error clicking on product:', e)

        try:
            add_cart_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Adicionar ao carrinho')))
            add_cart_btn.click()
            print('Produto adicionado ao carrinho')
        except Exception as e:
            print('Error clicking on "Adicionar ao carrinho":', e)

        try:
            cart_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continuar")')))
            cart_modal.click()
            print('Modal de carrinho clicado')
        except Exception as e:
            print('Error clicking on "Continuar" in cart modal:', e)

        try:
            add_all_items = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Tudo")')))
            add_all_items.click()
            print('Oppção de selecionar todos os produtos encontrada com sucesso')
        except Exception as e:
            print('Error clicking on "Tudo":', e)

        try:
            close_cart_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Finalizar compra')
            close_cart_btn.click()
            print('Carrinho finalizado')
        except Exception as e:
            print('Error clicking on "Finalizar compra":', e)

        try:
            continue_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continuar")')))
            continue_btn.click()
            print('Continuar encontrado com sucesso')
        except Exception as e:
            print('Error clicking on "Continuar":', e)

        try:
            payment_opt_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Método de pagamento, ')))
            payment_opt_btn.click()
            print('Método de pagamento encontrado com sucesso')
        except Exception as e:
            print('Error clicking on payment option button:', e)

        try:
            pix_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pix')))
            pix_opt.click()
            print('Opção de PIX selecionada')
        except Exception as e:
            print('Error selecting "Pix":', e)

        try:
            review_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Revisar pedido')))
            review_btn.click()
            print('Produto revisado')
        except Exception as e:
            print('Error clicking on "Revisar pedido":', e)

        try:
            self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=900, duration=800)
            time.sleep(1.2)
        except Exception as e:
            print('Error performing swipe:', e)

        try:
            confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Confirmar compra')
            confirm_btn.click()
            print('Compra confirmada')
        except Exception as e:
            print('Error clicking on "Confirmar compra":', e)

        try:
            time.sleep(2)
            self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=900, duration=800)
        except Exception as e:
            print('Error performing second swipe:', e)

        try:
            time.sleep(0.5)
            ok_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Ok')))
            ok_btn.click()
            print('Ok clicado com sucesso')
        except Exception as e:
            print('Error clicking "Ok":', e)

        try:
            sucess_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Continuar')))
            sucess_modal.click()
            print('Modal de sucesso fechado com sucesso')
        except Exception as e:
            print('Error clicking on "Continuar":', e)

        try:
            menu_btn.click()
            print('Menu clicado com sucesso')
        except Exception as e:
            print('Error clicking on "Menu":', e)

        try:
            my_purchases = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Meus Pedidos')))
            my_purchases.click()
            print('Listagem de compras')
        except Exception as e:
            print('Error clicking on "Meus Pedidos":', e)

        try:
            wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aguardando pagamento").instance(0)')))
            print('Compras encontradas com sucesso')
        except Exception as e:
            print('Error locating "Aguardando pagamento":', e)

        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()
