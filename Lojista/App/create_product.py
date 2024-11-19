"""
Create X amount of products
"""

import time
import os
import sys
import re
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
from Utils.person import (
    create_random_full_name,
    create_phone,
    create_birth_day
)

from Common.App.login import app_login

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
        
        app_login(wait, 'camisilvajk@gmail.com', self)
        
        for i in range(amount):
            add_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Adicionar")')))
            add_btn.click()
            
            prod_name = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o nome do produto")')))
            prod_name.send_keys(f'Batom automático {i + 1}')
            
            waring_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite os avisos sobre o produto")')
            waring_input.send_keys('Não ingerir!')
            
            loop_count = random.randint(2, 3)

            for img_loop in range(loop_count):
                add_image_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '+')))
                add_image_btn.click()
                
                galery_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ', Abrir galeria')))
                galery_opt.click()
                
                album_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Álbuns')))
                album_opt.click()
                download_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Downloads")')))
                download_opt.click()                                                                
                image = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance({img_loop+1})')))
                image.click()
                
                img_loop += 1
        
            rand_value = random.randint(16,20)
            value_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("R$ 000,00")')))
            value_input.send_keys(rand_value * 109)
            
            desc_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite a descrição do produto")')
            desc_input.send_keys('Um batom genérico.')
            
            det_desc_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite a descrição detalhada")')
            det_desc_input.send_keys('Um batom genérico é um produto cosmético utilizado para realçar os lábios, geralmente com textura cremosa, acabamento opaco ou brilhante, e disponível em diversas tonalidades.')
        
            self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=460, duration=800)
            color_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione as cores")')
            color_dropdown.send_keys('Preto')
            # color_dropdown.click()
            # self.driver.tap([(127, 566)])

            close_color = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Preto").instance(0)')))
            close_color.click()
            
            add_image_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '+')))
            add_image_btn.click()
            
            galery_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ', Abrir galeria')))
            galery_opt.click()
            
            album_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Álbuns')))
            album_opt.click()
            download_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Downloads")')))
            download_opt.click()                                                                
            image = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.providers.media.module:id/icon_thumbnail").instance(0)')))
            image.click()
            
            sizes_dropdown = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione o tamanho")')))
            sizes_dropdown.click()
            self.driver.tap([(131, 1097)])
            close_size = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Não se aplica")')))
            close_size.click()
            
            rand_width = random.randint(1, 100)
            width_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite a largura do produto")')
            width_input.send_keys(rand_width)

            rand_height = random.randint(1, 100)
            height_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o comprimento do produto")')
            height_input.send_keys(rand_height)

            self.driver.swipe(start_x=500, start_y=1933, end_x=500, end_y=1168, duration=800)
            category_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Selecione a categoria")')
            category_dropdown.click()
            self.driver.tap([(300, 1521)])
            
            sub_category_dropdown = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Selecione a subcategoria")')))
            sub_category_dropdown.click()
            self.driver.tap([(384, 1608)])
            
            model_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Digite o modelo do produto")')
            model_input.send_keys('Genérico')
            
            self.driver.swipe(start_x=500, start_y=2000, end_x=500, end_y=500, duration=800)
            voltage_dropdown = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Selecione a voltagem")')
            voltage_dropdown.click()
            self.driver.tap([(130, 670)])
            close_voltage = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nenhum")')))
            close_voltage.click()
            
            rand_stock = random.randint(5,100)
            stock_qnt = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Defina a quantidade em estoque")')
            stock_qnt.send_keys(rand_stock)
            
            prod_deadline_input = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Defina o prazo de produção")')
            prod_deadline_input.send_keys('1 dia')
            
            rand_garantees = random.choice([True, False])
            if rand_garantees == True:
                gar = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Garantia de fábrica")')
                gar.click()
                
                rand_gar_day = random.randint(1,30)
                gar_day_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00 dias")')))
                gar_day_input.send_keys(rand_gar_day)
                
                gar_store = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Garantia de loja")')
                gar_store.click()
                
                rand_gar_day = random.randint(1,30)
                gar_day_input = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("00 dias")')))
                gar_day_input.send_keys(rand_gar_day)
            else:
                no_gar = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Não tem")')
                no_gar.click()
                
            card_point = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pontua no cartão fidelidade")')
            card_point.click()
            
            time.sleep(0.8)
            save_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Salvar")')
            save_btn.click()
            
            continue_modal = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continuar")')))
            continue_modal.click()
            
            print(f'Product {i + 1} created')

        pending_list = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Pendentes')))
        pending_list.click()
        
if __name__ == '__main__':
    unittest.main()
