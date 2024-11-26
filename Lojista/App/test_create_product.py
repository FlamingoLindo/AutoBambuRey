"""
Create X amount of products
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

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Utils.get_user_input import get_user_input

from Common.App.lojista_login import app_lojista_login
from Common.App.add_lip_stick_images import add_lip_stick_images, add_color_image

class TestCreateProduct(unittest.TestCase):
    """
    Test case for automating the process of creating products.
    """

    amount = 0

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
        
    def test_02_create_product(self):
        amount = int(get_user_input('How many'))
        for i in range(amount):
            add_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Adicionar")')))
            add_btn.click()
            print('Botão "Adicionar" clicado.')

            prod_name = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o nome do produto")')))
            prod_name.send_keys(f'Batom automático {i + 1}')
            print('Nome do produto adicionado com sucesso')
        
            waring_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite os avisos sobre o produto")')
            waring_input.send_keys('Não ingerir!')
            print('Aviso adicionado com sucesso')

            add_lip_stick_images(wait)
        
            rand_value = random.randint(16,20)
            value_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("R$ 000,00")')))
            value_input.send_keys(rand_value * 109)
            print('Valor adicionado com sucesso')

            desc_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite a descrição do produto")')
            desc_input.send_keys('Um batom genérico.')
            print('Descrição adicionada com sucesso')

            det_desc_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite a descrição detalhada")')
            det_desc_input.send_keys(f'Descrição detalhada {i}')
            print('Descrição detalhada adicionada com sucesso')

            self.driver.swipe(start_x=500, start_y=1980, end_x=500, end_y=1250, duration=850)
            
            color_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione as cores")')
            color_dropdown.click()
            self.driver.tap([(130, 1460)])
            print('Cor selecionada com sucesso')

            close_color = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Amarelo").instance(0)')))
            close_color.click()
            print('Dropdown de cor fechado com sucesso')

            add_color_image(wait)
            
            sizes_dropdown = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione o tamanho")')))
            sizes_dropdown.click()
            self.driver.tap([(131, 2000)])
            print('Opção de tamanho selecionada com sucesso')

            close_size = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Não se aplica")')))
            close_size.click()
            print('Dropdown de tamanho fechado com sucesso')
                 
            self.driver.swipe(start_x=500, start_y=2060, end_x=500, end_y=850, duration=850)
            
            rand_width = random.randint(1, 100)
            width_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite a largura do produto")')
            width_input.send_keys(rand_width)
            print('Largura adicionada com sucesso')

            rand_height = random.randint(1, 100)
            height_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o comprimento do produto")')
            height_input.send_keys(rand_height)
            print('Comprimento adicionado com sucesso')

            category_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Selecione a categoria")')
            category_dropdown.click()
            self.driver.tap([(500, 1830)])
            print('Categoria adicionada com sucesso')
            
            sub_category_dropdown = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione a subcategoria")')))
            sub_category_dropdown.click()
            self.driver.tap([(500, 1890)])
            print('Subcategoria adicionada com sucesso')
                 
            model_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o modelo do produto")')
            model_input.send_keys('Genérico')
            print('Modelo adicionado com sucesso')

            self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=300, duration=850)
            
            voltage_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Selecione a voltagem")')
            voltage_dropdown.click()
            self.driver.tap([(130, 670)])
            print('Opção de voltagem adicionada com sucesso')
           
            close_voltage = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nenhum")')))
            close_voltage.click()
            print('Dropdown de voltagem fechado com sucesso')

            rand_stock = random.randint(5,100)
            stock_qnt = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Defina a quantidade em estoque")')
            stock_qnt.send_keys(rand_stock)
            print('Quantidade de estoque adicionada com sucesso')

            prod_deadline_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Defina o prazo de produção")')
            prod_deadline_input.send_keys('1 dia')
            print('Prazo adicionado com sucesso')

            rand_garantees = random.choice([True, False])
            if rand_garantees == True:
                
                gar = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Garantia de fábrica")')
                gar.click()
                print('Opção de garantia de fábrica ativada')

                rand_gar_day = random.randint(1,30)
                gar_day_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00 dias")')))
                gar_day_input.send_keys(rand_gar_day)
                print('Garantia de fábrica adicionada')

                gar_store = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Garantia de loja")')
                gar_store.click()
                print('Garantia de loja adicionada')

                rand_gar_day = random.randint(1,30)
                gar_day_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00 dias")')))
                gar_day_input.send_keys(rand_gar_day)
                print('Grantia adicionada')
                

            else:
                no_gar = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Não tem")')
                no_gar.click()
                print('Opção de sem garantia ativada')
    
                card_point = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pontua no cartão fidelidade")')
                card_point.click()
                print('Opção de cartão fidelidade ativada')
     
                time.sleep(0.8)
                save_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Salvar")')
                save_btn.click()
                print('Botão "Salver" clicado')

                continue_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continuar")')))
                continue_modal.click()
                print('Botão "Continuar" clicado')

            print(f'Product {i + 1} created.\n')

            pending_list = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pendentes')))
            pending_list.click()
        

if __name__ == '__main__':
    unittest.main()
