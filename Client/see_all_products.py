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
from appium.webdriver.extensions.android.nativekey import AndroidKey
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

from Common.adhajhda import teste

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
        see_all_catgs_btn.click()
        
        #
        gym_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Academia"))')))
        gym_opt.click()
        
        lutas_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Lutas')))
        lutas_opt.click()
        teste(self, wait, 'Lutas')
        
        cross_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Crossfit')))
        cross_opt.click()
        teste(self, wait, 'Crossfit')
                
        danca_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Dança')))
        danca_opt.click()
        teste(self, wait, 'Dança')
        
        nat_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Natação')))
        nat_opt.click()
        teste(self, wait, 'Natação')
        
        trein_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Treinamento Funcional')))
        trein_opt.click()
        teste(self, wait, 'Treinamento Funcional')
        
        another_button = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(14)')))
        time.sleep(1)
        another_button.click()
        
        #
        acessories_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Acessórios"))')))
        acessories_opt.click()
        
        colar_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'colar')))
        colar_opt.click()
        teste(self, wait, 'Colar')
        
        puls_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'pulseiras')))
        puls_opt.click()
        teste(self, wait, 'Pulseira')
        
        brin_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'brincos')))
        brin_opt.click()
        teste(self, wait, 'Brincos')
        
        body_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'body')))
        body_opt.click()
        teste(self, wait, 'Body')
        
        brac_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'braceletes')))
        brac_opt.click()
        teste(self, wait, 'Braceletes')
        
        pres_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Presilhas de cabelo')))
        pres_opt.click()
        teste(self, wait, 'Presilhas de cabelo')
        
        porta_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Porta jóia')))
        porta_opt.click()
        teste(self, wait, 'Porta joia')
        
        time.sleep(1)
        another_button.click()
        
        #
        adestrador_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Adestrador"))')))
        adestrador_opt.click()
        
        caes_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Cães')))
        caes_opt.click()
        teste(self, wait, 'Cães')
        
        gato_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Gato')))
        gato_opt.click()
        teste(self, wait, 'Gato')
        
        adestramento_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Adestramento básico')))
        adestramento_opt.click()
        teste(self, wait, 'Adestramento')
        
        adestramento2_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Adestramento de obediência')))
        adestramento2_opt.click()
        teste(self, wait, 'Adestramento 2')
        
        adestramento3_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Adestramento Avançado ')))
        adestramento3_opt.click()
        teste(self, wait, 'Adestramento 3')
        
        time.sleep(1)
        another_button.click()
        
        #
        advo_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Advocacia"))')))
        advo_opt.click()
        
        amb_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Direito Ambiental')))
        amb_opt.click()
        teste(self, wait, 'Ambiental')
        
        trab_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Direito Trabalhista')))
        trab_opt.click()
        teste(self, wait, 'Trabalhista')
        
        prev_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Direito Previdenciário')))
        prev_opt.click()
        teste(self, wait, 'Previdenciário')
        
        consumidor_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Direito do Consumidor')))
        consumidor_opt.click()
        teste(self, wait, 'Consumidor')
        
        trib_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Direito Tributário')))
        trib_opt.click()
        teste(self, wait, 'Tributário')
        
        fam_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Direito da família')))
        fam_opt.click()
        teste(self, wait, 'Familia')
        
        imo_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Direito imobiliário')))
        imo_opt.click()
        teste(self, wait, 'Imobiliária')
        
        penal_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, ' Direito penal')))
        penal_opt.click()
        teste(self, wait, 'Penal')
        
        time.sleep(1)
        another_button.click()
        
        #
        ali_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Alimentos e bebidas"))')))
        ali_opt.click()
        
        alim_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Alimentos e bebidas não alcoólicas')))
        alim_opt.click()
        teste(self, wait, 'Alimentos')

        produtos_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Produtos naturais e orgânicos')))
        produtos_opt.click()
        teste(self, wait, 'Produtos')
        
        time.sleep(1)
        another_button.click()
        
        #
        car_rental_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Aluguel de carro"))')))
        car_rental_opt.click()
        
        rental_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Aluguel - quando o veículo é utilizado para transporte remunerado de carga ou passageiro (placa vermelha)')))
        rental_opt.click()
        teste(self, wait, 'Aluguel')
        
        private_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Particular - quando o veículo é utilizado para fins particulares (placa cinza).')))
        private_opt.click()
        teste(self, wait, 'Privado')
        
        time.sleep(1)
        another_button.click()
        
        #
        suit_rental_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Aluguel de Trajes e Fantasias"))')))
        suit_rental_opt.click()
        
        rental_roupa_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Aluguel de roupas para eventos')))
        rental_roupa_opt.click()
        teste(self, wait, 'Roupas')
        
        rental_fantasia_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Aluguel de fantasia para festas temáticas')))
        rental_fantasia_opt.click()
        teste(self, wait, 'Fantasia')
        
        rental_sub_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Aluguel de roupas por assinatura')))
        rental_sub_opt.click()
        teste(self, wait, 'Assinatura')
        
        time.sleep(1)
        another_button.click()
        
        #
        arch_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Arquiteto"))')))
        arch_opt.click()
        
        proj_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Projeto Arquitetônico')))
        proj_opt.click()
        teste(self, wait, 'Arquitetônico')
        
        interior_design_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Design de Interiores')))
        interior_design_opt.click()
        teste(self, wait, 'Design')
        
        proj_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Gestão de Obras ou Gerenciamento de Projetos')))
        proj_opt.click()
        teste(self, wait, 'Gestão')
        
        paisagem_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Paisagismo ou projetos de áreas externas')))
        paisagem_opt.click()
        teste(self, wait, 'Paisagismo')
        
        time.sleep(1)
        another_button.click()
        
        #
        party_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Artigos de festa"))')))
        party_opt.click()
        
        batizado_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'batizado')))
        batizado_opt.click()
        teste(self, wait, 'Batizado')
        
        casamento_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'casamento')))
        casamento_opt.click()
        teste(self, wait, 'Casamento')
        
        aniversario_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'aniversario')))
        aniversario_opt.click()
        teste(self, wait, 'Aniversario')
        
        cha_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'chá de bebe')))
        cha_opt.click()
        teste(self, wait, 'Chá')
        
        ano_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'ano novo')))
        ano_opt.click()
        teste(self, wait, 'Ano')
        
        natal_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'natal')))
        natal_opt.click()
        teste(self, wait, 'Natal')
        
        time.sleep(1)
        another_button.click()
        
        #
        assist_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Assistência técnica"))')))
        assist_opt.click()
        
        celular_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Celular')))
        celular_opt.click()
        teste(self, wait, 'Celular')
    
        time.sleep(1)
        another_button.click()
        
        #
        baba_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Babá"))')))
        baba_opt.click()
        
        diurna_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Babá diurna')))
        diurna_opt.click()
        teste(self, wait, 'Diurna')
        
        noturna_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Babá noturna')))
        noturna_opt.click()
        teste(self, wait, 'Noturna')
        
        maternidade_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Babá de maternidade')))
        maternidade_opt.click()
        teste(self, wait, 'Maternidade')
    
        time.sleep(1)
        another_button.click()
        
        #
        barbearia_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().text("Barbearia"))')))
        barbearia_opt.click()
        
        cortes_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Cortes')))
        cortes_opt.click()
        teste(self, wait, 'Cortes')
        
        estili_opt = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Estilização de cabelos e barbas')))
        estili_opt.click()
        teste(self, wait, 'Estilização')


        time.sleep(1)
        another_button.click()
                
if __name__ == '__main__':
    unittest.main()
