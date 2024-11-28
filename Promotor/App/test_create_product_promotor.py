"""
Create a X amount of products by the "Promotor" user.
"""

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
from selenium.common.exceptions import TimeoutException

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Utils.get_user_input import get_user_input

from Common.App.add_lip_stick_images import add_lip_stick_images_promotor, add_color_image_promotor

TEST_TITLE = 'CRIAÇÃO DE PRODUTO PROMOTOR'
QA = 'Vitor Flamingo Lindo'
BACK = 'Lucas Lizo'
MOBILE = 'Luciano Esponjas'

class TestCreateProductPromotor(unittest.TestCase):
    """
    Test case for automating the process of creating products.
    """
    
    def setUp(self) -> None:
        capabilities = dict(
        noReset=True,
        automationName='uiautomator2',
        language='pt',
        printPageSourceOnFindFailure=True,
        appPackage='com.mestresdaweb.bambureypromotor',
        appActivity='com.mestresdaweb.bambureypromotor.MainActivity'
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
        email_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Digite seu e-mail")')))
        email_input.send_keys(os.getenv('PRO_EMAIL'))

        password = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Digite sua senha")')
        password.send_keys(os.getenv('PRO_PASS'))

        login_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Entrar")')
        login_btn.click()
        
        try:
            # Wait for the error message if it appears
            error_msg = wait.until(EC.visibility_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Email Inválido")')
            ))
            # If the error message appears, assert failure
            assert False, error_msg.text == 'Email Inválido'; f"Unexpected error message: {error_msg.text}"
        except TimeoutException:
            # No error message, login is successful
            print('E-mail e senha corretos')
            print('Login realizado com sucesso!')
        
    def test_02_close_bank(self):
        """
        Test close bank modal
        """
        bank_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ir")')))
        assert bank_modal.is_displayed(), 'Promotor tem conta bancária'
        bank_modal.click() 
        
        go_back_arrow = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')))
        assert go_back_arrow.is_displayed(), 'Botão de "Voltar" não encontrado'
        go_back_arrow.click()
        
    def test_03_open_store(self):
        """
        Test open "Lojas" page
        """
        stores_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Lojas')))
        assert stores_btn.is_displayed(), 'Botão "Lojas" não encontrado'
        stores_btn.click()
        
        select_store = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Flamingo")')))
        select_store.click()
        
    def test_04_create_product(self):
        """
        Test create X amount of products
        """
        amount = int(get_user_input('How many'))
        for i in range(amount):
            add_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ', Cadastrar produto')))
            assert add_btn.is_displayed(), 'Botão "Cadastrar" não encontrado!'
            add_btn.click()
            print('Botão "Adicionar" clicado.')

            prod_name = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')))
            prod_name.send_keys(f'Batom automático {i + 1}')
            print('Nome do produto adicionado com sucesso')
        
            waring_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            waring_input.send_keys('Não ingerir!')
            print('Aviso adicionado com sucesso')

            add_lip_stick_images_promotor(wait)

            time.sleep(0.5)
            
            desc_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            desc_input.send_keys('Um batom genérico.')
            print('Descrição adicionada com sucesso')
            
            det_desc_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')
            det_desc_input.send_keys(f'Descrição detalhada {i+1}')
            print('Descrição detalhada adicionada com sucesso')
        
            rand_value = random.randint(16,20)
            value_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite aqui...").instance(0)')))
            value_input.send_keys(rand_value * 109)
            print('Valor adicionado com sucesso')

            self.driver.swipe(start_x=500, start_y=1980, end_x=500, end_y=1250, duration=850)
            
            rand_width = random.randint(1, 100)
            width_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite a largura do produto")')
            width_input.send_keys(rand_width)
            print('Largura adicionada com sucesso')

            rand_height = random.randint(1, 100)
            height_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o comprimento do produto")')
            height_input.send_keys(rand_height)
            print('Comprimento adicionado com sucesso')
            
            sizes_dropdown = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione os tamanhos")')))
            sizes_dropdown.click()
            self.driver.tap([(139, 2036)])
            print('Opção de tamanho selecionada com sucesso')

            close_size = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Único (36 ao 42)")')))
            close_size.click()
            print('Dropdown de tamanho fechado com sucesso')
            
            self.driver.swipe(start_x=500, start_y=2060, end_x=500, end_y=850, duration=850)
            
            color_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione as cores")')
            color_dropdown.click()
            self.driver.tap([(139, 790)])
            print('Cor selecionada com sucesso')

            close_color = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Preto").instance(0)')))
            close_color.click()
            print('Dropdown de cor fechado com sucesso')

            add_color_image_promotor(wait)

            voltage_dropdown = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Selecione as voltagens")')))
            voltage_dropdown.click()
            self.driver.tap([(140, 1414)])
            print('Opção de voltagem adicionada com sucesso')
           
            close_voltage = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nenhum")')))
            close_voltage.click()
            print('Dropdown de voltagem fechado com sucesso')
            
            time.sleep(0.5)
            
            # model_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" ").instance(0)')
            # model_input.send_keys('Genérico')
            # print('Modelo adicionado com sucesso')
            
            # brand_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" ").instance(0)')
            # brand_input.send_keys('Marca Genérica')
            # print('Marca adicionada com sucesso')
            
            rand_stock = random.randint(5,100)
            stock_qnt = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Defina a quantidade em estoque")')
            stock_qnt.send_keys(rand_stock)
            print('Quantidade de estoque adicionada com sucesso')
            
            self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=300, duration=850)
            
            prod_deadline_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(" ")')
            prod_deadline_input.send_keys('1 dia')
            print('Prazo adicionado com sucesso')
            
            rand_garantees = random.choice([True, False])
            if rand_garantees == True:
                fact_garant = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(17)')
                fact_garant.click()
                days_input = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00 dias")')))
                days_input.send_keys(random.randint(1,31))
                
                store_garant = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(19)')
                store_garant.click()
                days_input = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00 dias")')))
                days_input.send_keys(random.randint(1,31))
            
            else:
                no_garant = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(19)')
                no_garant.click()
                    
            category_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Selecione a categoria")')
            time.sleep(0.5)
            category_dropdown.click()
            self.driver.tap([(238, 1675)])
            print('Categoria adicionada com sucesso')
            
            time.sleep(2)
            
            sub_category_dropdown = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione a subcategoria")')))
            time.sleep(0.5)
            sub_category_dropdown.click()
            self.driver.tap([(384, 1921)])
            print('Subcategoria adicionada com sucesso')
                 
            time.sleep(1)
            
            publish_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Publicar")')
            assert publish_btn.is_displayed(), 'Botão "Salvar" não encontrado!'
            publish_btn.click()
            print('Botão "Salvar" clicado')
            
            continue_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Fechar")')))
            assert continue_modal.is_displayed, 'Modal não encontrado'
            continue_modal.click()
            print('Botão "Fechar" clicado')

            print(f'Product {i + 1} created.\n')

if __name__ == '__main__':
    unittest.main()
