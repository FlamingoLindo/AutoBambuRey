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
from appium.webdriver.extensions.android.nativekey import AndroidKey

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from Utils.get_user_input import get_user_input

from Common.App.lojista_login import app_lojista_login
from Common.App.add_lip_stick_images import add_lip_stick_images, add_color_image

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

    def test_create_product(self) -> None:
        """
        """
        amount = int(get_user_input('How many'))
        
        wait = WebDriverWait(self.driver, 10)
        
        app_lojista_login(wait, 'camisilvajk@gmail.com', self)
        
        for i in range(amount):
            try:
                add_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Adicionar")')))
                add_btn.click()
                print('Botão "Adicionar" clicado.')
            except Exception as e:
                print('Error in the "Add button".\n', e)
            
            try:
                prod_name = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o nome do produto")')))
                prod_name.send_keys(f'Batom automático {i + 1}')
                print('Nome do produto adicionado com sucesso')
            except Exception as e:
                print('Error in "Name" input.\n', e)
            
            try:
                waring_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite os avisos sobre o produto")')
                waring_input.send_keys('Não ingerir!')
                print('Aviso adicionado com sucesso')
            except Exception as e:
                print('Error in "Warning" input.\n', e)
            
            add_lip_stick_images(wait)
        
            try:
                rand_value = random.randint(16,20)
                value_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("R$ 000,00")')))
                value_input.send_keys(rand_value * 109)
                print('Valor adicionado com sucesso')
            except Exception as e:
                print('Error in "Valor" input.\n', e)
                
            try:
                desc_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite a descrição do produto")')
                desc_input.send_keys('Um batom genérico.')
                print('Descrição adicionada com sucesso')
            except Exception as e:
                print('Error in "Descrição" input.\n', e)
                
            try:
                det_desc_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite a descrição detalhada")')
                det_desc_input.send_keys(f'Descrição detalhada {i}')
                print('Descrição detalhada adicionada com sucesso')
            except Exception as e:
                print('Error in "Descrição detalhada" input.\n', e)
                
            self.driver.swipe(start_x=500, start_y=1980, end_x=500, end_y=1250, duration=850)
            try:
                color_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione as cores")')
                color_dropdown.click()
                self.driver.tap([(130, 1460)])
                print('Cor selecionada com sucesso')
            except Exception as e:
                print('Error in "Cor" select.\n', e)

            try:
                close_color = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Amarelo").instance(0)')))
                close_color.click()
                print('Dropdown de cor fechado com sucesso')
            except Exception as e:
                print('Error in closing field "Cor".\n', e)
            
            add_color_image(wait)
            
            try:
                sizes_dropdown = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione o tamanho")')))
                sizes_dropdown.click()
                self.driver.tap([(131, 2000)])
                print('Opção de tamanho selecionada com sucesso')
            except Exception as e:
                print('Error in openning "Tamanho" dropdown.\n', e)
                
            try:
                close_size = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Não se aplica")')))
                close_size.click()
                print('Dropdown de tamanho fechado com sucesso')
            except Exception as e:
                print('Error in closing "Tamanho" dropdown.\n', e)
            
            self.driver.swipe(start_x=500, start_y=2060, end_x=500, end_y=850, duration=850)
            
            try:
                rand_width = random.randint(1, 100)
                width_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite a largura do produto")')
                width_input.send_keys(rand_width)
                print('Largura adicionada com sucesso')
            except Exception as e:
                print('Error in sending "Largura".\n', e)

            try:
                rand_height = random.randint(1, 100)
                height_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o comprimento do produto")')
                height_input.send_keys(rand_height)
                print('Comprimento adicionado com sucesso')
            except Exception as e:
                print('Error in sending "Comprimento".\n', e)

            try:
                category_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Selecione a categoria")')
                category_dropdown.click()
                self.driver.tap([(500, 1830)])
                print('Categoria adicionada com sucesso')
            except Exception as e:
                print('Error in "Categoria".\n', e)
            
            try:
                sub_category_dropdown = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione a subcategoria")')))
                sub_category_dropdown.click()
                self.driver.tap([(500, 1890)])
                print('Subcategoria adicionada com sucesso')
            except Exception as e:
                print('Error in "Subcategoria".\n', e)
            
            try:
                model_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o modelo do produto")')
                model_input.send_keys('Genérico')
                print('Modelo adicionado com sucesso')
            except Exception as e:
                print('Error in "Modelo".\n', e)
            
            self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=300, duration=850)
            try:
                voltage_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Selecione a voltagem")')
                voltage_dropdown.click()
                self.driver.tap([(130, 670)])
                print('Opção de voltagem adicionada com sucesso')
            except Exception as e:
                print('Error in "Voltagem" option.\n', e)
            
            try:
                close_voltage = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nenhum")')))
                close_voltage.click()
                print('Dropdown de voltagem fechado com sucesso')
            except Exception as e:
                print('Error in closing "Voltagem".\n', e)
            
            try:
                rand_stock = random.randint(5,100)
                stock_qnt = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Defina a quantidade em estoque")')
                stock_qnt.send_keys(rand_stock)
                print('Quantidade de estoque adicionada com sucesso')
            except Exception as e:
                print('Error in "Estoque".\n', e)
            
            try:
                prod_deadline_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Defina o prazo de produção")')
                prod_deadline_input.send_keys('1 dia')
                print('Prazo adicionado com sucesso')
            except Exception as e:
                print('Error in "Prazo".\n', e)
            
            rand_garantees = random.choice([True, False])
            if rand_garantees == True:
                try:
                    gar = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Garantia de fábrica")')
                    gar.click()
                    print('Opção de garantia de fábrica ativada')
                except Exception as e:
                    print('Error in "Garantia da fábrica".\n', e)
                
                try:
                    rand_gar_day = random.randint(1,30)
                    gar_day_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00 dias")')))
                    gar_day_input.send_keys(rand_gar_day)
                    print('Garantia de fábrica adicionada')
                except Exception as e:
                    print('Error in "Garantia da fábrica" input.\n', e)
                
                try:
                    gar_store = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Garantia de loja")')
                    gar_store.click()
                    print('Garantia de loja adicionada')
                except Exception as e:
                    print('Error in "Garantia de loja".\n', e)
                
                try:
                    rand_gar_day = random.randint(1,30)
                    gar_day_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00 dias")')))
                    gar_day_input.send_keys(rand_gar_day)
                    print('Grantia adicionada')
                except Exception as e:
                    print('Error in "Garantia de loja" input.\n', e)
            else:
                try:
                    no_gar = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Não tem")')
                    no_gar.click()
                    print('Opção de sem garantia ativada')
                except Exception as e:
                    print('Error in "Não tem".\n', e)
            
            try:
                card_point = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pontua no cartão fidelidade")')
                card_point.click()
                print('Opção de cartão fidelidade ativada')
            except Exception as e:
                    print('Error in "Cartão fidelidade".\n', e)
            
            try:
                time.sleep(0.8)
                save_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Salvar")')
                save_btn.click()
                print('Botão "Salver" clicado')
            except Exception as e:
                    print('Error in "Salvar".\n', e)
            
            try:
                continue_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continuar")')))
                continue_modal.click()
                print('Botão "Continuar" clicado')
            except Exception as e:
                    print('Error in "Continuar".\n', e)
            
            print(f'Product {i + 1} created.\n')

        try:
            pending_list = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pendentes')))
            pending_list.click()
        except Exception as e:
                    print('Error in "Pendentes".\n', e)
        
if __name__ == '__main__':
    unittest.main()
