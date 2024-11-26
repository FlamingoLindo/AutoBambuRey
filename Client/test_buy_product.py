import time
import os
import sys
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

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

class TestCreateProductClient(unittest.TestCase):
    """
    Test case for automating the process of creating users and 
    testing the app's registration process.
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
        wait = WebDriverWait(self.driver, 5)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_01_open_app(self) -> None:
        """
        Test that the menu button is visible and clickable.
        """
        time.sleep(6)
        
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
        email.send_keys('flamingolindo1@gmail.com')

        password = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite sua senha")')))
        password.send_keys('Aa12345678!')

        log_in = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Entrar")')
        log_in.click()
        print('Logged in successfully')

    def test_03_search_product(self) -> None:
        """
        Test searching for a product.
        """
        search_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pesquisar por nome/id do produto')))
        search_btn.click()

        search_input = wait.until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, 'android.widget.EditText')))
        assert search_input.is_displayed(), "Search input field is not visible"
        search_input.send_keys('Minions')
        print('Search for product completed')

    def test_04_add_product_to_cart(self) -> None:
        """
        Test adding a product to the cart.
        """
        click_product = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Minions, R$ 6,00, 354')))
        click_product.click()

        add_cart_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Adicionar ao carrinho")')))
        add_cart_btn.click()
        assert add_cart_btn.text == 'Adicionar ao carrinho', 'Cart button text is wrong'
        print('Product added to cart successfully')

    def test_05_checkout(self) -> None:
        """
        Test the checkout process.
        """
        cart_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Continuar')))
        if cart_modal.is_displayed():
            cart_modal.click()
            print('Modal de carrinho clicado')
        else:
            print('Modal is not showing')
            assert False, 'No modal is displayed!'

        add_all_items = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Tudo")')))
        add_all_items.click()

        close_cart_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Finalizar compra')
        close_cart_btn.click()

        continue_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continuar")')))
        continue_btn.click()

        payment_opt_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Método de pagamento, ')))
        payment_opt_btn.click()

        pix_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pix')))
        pix_opt.click()

        review_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Revisar pedido')))
        review_btn.click()
        print('Review and payment method selected')
        
        try:
           toast_error = wait.until(EC.visibility_of_element_located(
               (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("toastContentContainer")')
           ))
           
           if toast_error.is_displayed():
               print('Erro de distancia')
               assert False, 'Distance error - Toast message displayed!'

        except Exception as e:
            print('No distance error toast found.')
            pass
        
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(535, 2206)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(570, 958)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(0.5)

        confirm_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Confirmar compra')
        if confirm_btn.is_displayed():
            confirm_btn.click()
            print('Compra confirmada')
        else:
            print('Botão de confirmar compra não encontrado')
            assert False, 'No "Confirmar compra" button'
    
        try:
            toast_error = wait.until(EC.visibility_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("toastContentContainer"')
            ))
            
            if toast_error.is_displayed():
                print('Erro no pagamento\n', toast_error.text)
                assert False, 'Payment error - Toast message displayed!'

        except Exception as e:
            print('No error toast found.')
            pass
        
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(535, 2206)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(570, 958)
        actions.w3c_actions.pointer_action.release()
        actions.perform()


        time.sleep(2)
        ok_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Ok')))
        ok_btn.click()
        print('OK clicked successfully')

        sucess_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Continuar')))
        sucess_modal.click()
        print('Success modal closed successfully')
    
    def test_06_purchase(self) -> None:
        menu_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Menu')))
        assert menu_btn.is_displayed(), "Menu button is not visible"
        print('Menu encontrado')
        menu_btn.click()

        my_purchases = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Meus Pedidos')))
        my_purchases.click()
        print('Listagem de compras')

        wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aguardando pagamento").instance(0)')))
        print('Compras encontradas com sucesso')
        
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
