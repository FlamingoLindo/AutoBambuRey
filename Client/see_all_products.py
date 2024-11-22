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
from selenium.common.exceptions import TimeoutException

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_to_add)

capabilities = dict(
    noReset=False,
    automationName='uiautomator2',
    language='pt',
    printPageSourceOnFindFailure=True,
    appPackage='com.mestresdaweb.bamburey',
    appActivity='com.mestresdaweb.bamburey.MainActivity'
)

from Common.adhajhda import teste, app_scroll, select_category_and_subcategories

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

    def test_see_all_products(self) -> None:
        """
        
        """
        
        wait = WebDriverWait(self.driver, 7)
        
        time.sleep(6)
        
        wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Menu')))
                
        end_x_ = 500
        end_y_ = 1630
        while True:
            try:
                all_ad = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0 Vendido(s)")')))
                print('Ad found in the "Tudo" tab!')
                break
            except TimeoutException:
                print('No ad found, trying to find it again...')
                end_x_ -= 150  
                end_y_ -= 150  
                self.driver.swipe(start_x=543, start_y=1630, end_x=end_x_, end_y=end_y_, duration=90)

        news_opt = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Novidades"))')))
        news_opt.click()
        end_x_ = 500
        end_y_ = 1630
        while True:
            try:
                all_ad = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("0 Vendido(s)")')))
                print('Ad found in the "Novidades" tab!')
                break
            except TimeoutException:
                print('No ad found, trying to find it again...')
                end_x_ -= 150  
                end_y_ -= 150  
                self.driver.swipe(start_x=543, start_y=1630, end_x=end_x_, end_y=end_y_, duration=90)
                
        
        see_all_catgs_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Ver mais"))')))
        time.sleep(0.4)
        see_all_catgs_btn.click()
        
        #
        category_locator = AppiumBy.ANDROID_UIAUTOMATOR
        category_value = "Academia"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Lutas"),
            (AppiumBy.ACCESSIBILITY_ID, "Crossfit"),
            (AppiumBy.ACCESSIBILITY_ID, "Dança"),
            (AppiumBy.ACCESSIBILITY_ID, "Natação"),
            (AppiumBy.ACCESSIBILITY_ID, "Treinamento Funcional")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        # 
        category_value = "Acessórios" 
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "colar"),
            (AppiumBy.ACCESSIBILITY_ID, "pulseiras"),
            (AppiumBy.ACCESSIBILITY_ID, "brincos"),
            (AppiumBy.ACCESSIBILITY_ID, "body"),
            (AppiumBy.ACCESSIBILITY_ID, "braceletes"),
            (AppiumBy.ACCESSIBILITY_ID, "Presilhas de cabelo"),
            (AppiumBy.ACCESSIBILITY_ID, "Porta jóia")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Adestrador"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Cães"),
            (AppiumBy.ACCESSIBILITY_ID, "Gato"),
            (AppiumBy.ACCESSIBILITY_ID, "Adestramento básico"),
            (AppiumBy.ACCESSIBILITY_ID, "Adestramento de obediência"),
            (AppiumBy.ACCESSIBILITY_ID, "Adestramento Avançado")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Advocacia"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Direito Ambiental"),
            (AppiumBy.ACCESSIBILITY_ID, "Direito Trabalhista"),
            (AppiumBy.ACCESSIBILITY_ID, "Direito Previdenciário"),
            (AppiumBy.ACCESSIBILITY_ID, "Direito do Consumidor"),
            (AppiumBy.ACCESSIBILITY_ID, "Direito Tributário"),
            (AppiumBy.ACCESSIBILITY_ID, "Direito da família"),
            (AppiumBy.ACCESSIBILITY_ID, "Direito imobiliário"),
            (AppiumBy.ACCESSIBILITY_ID, "Direito penal")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
   
        #
        category_value = "Alimentos e bebidas"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Alimentos e bebidas não alcoólicas"),
            (AppiumBy.ACCESSIBILITY_ID, "Produtos naturais e orgânicos")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
              
        # 
        category_value = "Aluguel de carro"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Aluguel - quando o veículo é utilizado para transporte remunerado de carga ou passageiro (placa vermelha)"),
            (AppiumBy.ACCESSIBILITY_ID, "Particular - quando o veículo é utilizado para fins particulares (placa cinza).")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Aluguel de Trajes e Fantasias"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Aluguel de roupas para eventos"),
            (AppiumBy.ACCESSIBILITY_ID, "Aluguel de fantasia para festas temáticas"),
            (AppiumBy.ACCESSIBILITY_ID, "Aluguel de roupas por assinatura")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Arquiteto"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Projeto Arquitetônico"),
            (AppiumBy.ACCESSIBILITY_ID, "Design de Interiores"),
            (AppiumBy.ACCESSIBILITY_ID, "Gestão de Obras ou Gerenciamento de Projetos"),
            (AppiumBy.ACCESSIBILITY_ID, "Paisagismo ou projetos de áreas externas")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        # 
        category_value = "Artigos de festa"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "batizado"),
            (AppiumBy.ACCESSIBILITY_ID, "casamento"),
            (AppiumBy.ACCESSIBILITY_ID, "aniversario"),
            (AppiumBy.ACCESSIBILITY_ID, "chá de bebe"),
            (AppiumBy.ACCESSIBILITY_ID, "ano novo"),
            (AppiumBy.ACCESSIBILITY_ID, "natal")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        # 
        category_value = "Assistência técnica"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Celular")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        # 
        category_value = "Babá"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Babá diurna"),
            (AppiumBy.ACCESSIBILITY_ID, "Babá noturna"),
            (AppiumBy.ACCESSIBILITY_ID, "Babá de maternidade")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Barbearia"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Cortes"),
            (AppiumBy.ACCESSIBILITY_ID, "Estilização de cabelos e barbas")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
          
        #
        app_scroll(wait,self,AppiumBy.ACCESSIBILITY_ID,'Borracharia')

        #
        category_value = "beleza e cuidados pessoais "
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Suplementos e vitaminas"),
            (AppiumBy.ACCESSIBILITY_ID, "Cosméticos e maquiagem"),
            (AppiumBy.ACCESSIBILITY_ID, "Perfumes e fragrâncias"),
            (AppiumBy.ACCESSIBILITY_ID, "Produtos de higiene")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "bolsas e mochilas"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Mochilas "),
            (AppiumBy.ACCESSIBILITY_ID, "Bolsas")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        # 
        category_value = "Borracharia"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Conserto e troca de pneus avariados")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        # 
        category_value = "Brinquedos"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Bonecas"),
            (AppiumBy.ACCESSIBILITY_ID, "Brinquedos educativos"),
            (AppiumBy.ACCESSIBILITY_ID, "Brinquedos infláveis"),
            (AppiumBy.ACCESSIBILITY_ID, "Bonecos"),
            (AppiumBy.ACCESSIBILITY_ID, "Jogos"),
            (AppiumBy.ACCESSIBILITY_ID, "Brinquedos de Montar"),
            (AppiumBy.ACCESSIBILITY_ID, "Fantasias")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
                
        #
        category_value = "Cabelereiro(a)"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Cortes, escova.")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        

        time.sleep(10)
        #another_button.click()
        
                
if __name__ == '__main__':
    unittest.main()
