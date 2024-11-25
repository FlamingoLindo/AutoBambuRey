"""
This module is used for openning all categories and subcategories.
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
        wait = WebDriverWait(self.driver, 5)
        
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
        app_scroll(self.driver)
        print('cabelo')

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
        
        #
        time.sleep(1)
        app_scroll(self.driver)
        print('Controle de pragas')

        #
        category_value = "Cartórios"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Resgistro Civil"),
            (AppiumBy.ACCESSIBILITY_ID, "Tabelionatos de notas"),
            (AppiumBy.ACCESSIBILITY_ID, "Registro de imóveis"),
            (AppiumBy.ACCESSIBILITY_ID, "Registro de títulos e documentos"),
            (AppiumBy.ACCESSIBILITY_ID, "Registro de distribuição"),
            (AppiumBy.ACCESSIBILITY_ID, "Tabelionato de protesto"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Casa e cozinha"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Cama, Mesa e Banho ( Lençóis, Toalhas e Travesseiros)"),
            (AppiumBy.ACCESSIBILITY_ID, "Artigos de decoração"),
            (AppiumBy.ACCESSIBILITY_ID, "Iluminação"),
            (AppiumBy.ACCESSIBILITY_ID, "Móveis"),
            (AppiumBy.ACCESSIBILITY_ID, "Organização e armazenamento"),
            (AppiumBy.ACCESSIBILITY_ID, "Garras térmicas"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Chaveiro"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Cópias de chaves"),
            (AppiumBy.ACCESSIBILITY_ID, "Chaveiros e carimbos")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Churrasqueiro"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Festas e eventos")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Confeitarias"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Encomendas"),
            (AppiumBy.ACCESSIBILITY_ID, "Produtos para confeitaria")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Controle de pragas"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Dedetização"),
            (AppiumBy.ACCESSIBILITY_ID, "Desratização")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        time.sleep(1)
        app_scroll(self.driver)
        print('Eletricista')

        #
        category_value = "Correio"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Serviços")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Cozinheiro(a)"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Festas e eventos"),
            (AppiumBy.ACCESSIBILITY_ID, "Personal Chef")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Dentista"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Odontopediatria"),
            (AppiumBy.ACCESSIBILITY_ID, "Ortodontia"),
            (AppiumBy.ACCESSIBILITY_ID, "Odontologia Estética"),
            (AppiumBy.ACCESSIBILITY_ID, "Clínico geral"),
            (AppiumBy.ACCESSIBILITY_ID, "Periodontista"),
            (AppiumBy.ACCESSIBILITY_ID, "Implantodontia"),
            (AppiumBy.ACCESSIBILITY_ID, "Estomatologista")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
                
        
        category_value = "Designer de interiores"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Projetos residenciais"),
            (AppiumBy.ACCESSIBILITY_ID, "Projetos Comerciais")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Diarista"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Passadeira"),
            (AppiumBy.ACCESSIBILITY_ID, "Serviço de limpeza"),
            (AppiumBy.ACCESSIBILITY_ID, "Serviços Gerias")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Eletricista"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Eletrecista Geral"),
            (AppiumBy.ACCESSIBILITY_ID, "Eletrecista de coifa e depurador"),
            (AppiumBy.ACCESSIBILITY_ID, "Novas instalações elétricas")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        time.sleep(1)
        app_scroll(self.driver)
        print('Engenharia')
        
        #
        category_value = "Eletrodomésticos e utilidades domésticas"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Aspiradores, Ferros de passar, Aparelhos de limpeza"),
            (AppiumBy.ACCESSIBILITY_ID, "Geladeiras, Freezers e Frigobares"),
            (AppiumBy.ACCESSIBILITY_ID, "Fogões, Fornos e Microondas"),
            (AppiumBy.ACCESSIBILITY_ID, "Lavadouras, Secadouras e Lava-louças"),
            (AppiumBy.ACCESSIBILITY_ID, "Ventiladores, Climatizadores e Aquecedores"),
            (AppiumBy.ACCESSIBILITY_ID, "Utensílios de Cozinha, Panelas, Talheres e Eletroportáteis"),
            (AppiumBy.ACCESSIBILITY_ID, "Purificadores e Filtros de água"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Eletrônicos e tecnologia"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Smartphones, Tablets, Acessórios"),
            (AppiumBy.ACCESSIBILITY_ID, "TVs, Áudio, Home theater, Vídeo"),
            (AppiumBy.ACCESSIBILITY_ID, "Fones e Smart whatchs"),
            (AppiumBy.ACCESSIBILITY_ID, "Computadores, Notebooks e Periféricos"),
            (AppiumBy.ACCESSIBILITY_ID, "Gadgets e Wearables"),
            (AppiumBy.ACCESSIBILITY_ID, "Impressoras, Scaners e Suprimentos"),
            (AppiumBy.ACCESSIBILITY_ID, "Rede e Conectividade(Modens e Roteadores)"),
            (AppiumBy.ACCESSIBILITY_ID, "Câmeras, Drones e acessórios"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Empregada doméstica"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Serviços domésticos em geral.")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Encanador"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Instalação de sistemas hidrálicos de água e esgoto em residências, prédios e indústrias"),
            (AppiumBy.ACCESSIBILITY_ID, "Manutenção de sistemas didráulicos"),
            (AppiumBy.ACCESSIBILITY_ID, "Reparo de vazamentos inesperados, como em torneiras, válvulas de descarga ou ruptura de tubulação")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Enfermagem"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Enfermagem domiciliar"),
            (AppiumBy.ACCESSIBILITY_ID, "Acompanhamento pós operatório"),
            (AppiumBy.ACCESSIBILITY_ID, "Acompanhamento Hospitalar"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        
        category_value = "Engenharia"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Engenharia Civil"),
            (AppiumBy.ACCESSIBILITY_ID, "Engenharia Mecânica"),
            (AppiumBy.ACCESSIBILITY_ID, "Engenharia Elétrica")
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        time.sleep(1)
        app_scroll(self.driver)
        print('Engenharia')

        #
        category_value = "Escolas"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Educação Infantil"),
            (AppiumBy.ACCESSIBILITY_ID, "Ensino Fundamental"),
            (AppiumBy.ACCESSIBILITY_ID, "Ensino Médio"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Esportes e lazer"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Tênis"),
            (AppiumBy.ACCESSIBILITY_ID, "Equipamento para esportes"),
            (AppiumBy.ACCESSIBILITY_ID, "Roupas e acessórios"),
            (AppiumBy.ACCESSIBILITY_ID, "Bicicletas, Patins, Skate"),
            (AppiumBy.ACCESSIBILITY_ID, "Equipamento de pesca"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Farmácia"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Medicamentos"),
            (AppiumBy.ACCESSIBILITY_ID, "Vitaminas e Suplementos"),
            (AppiumBy.ACCESSIBILITY_ID, "Cosméticos"),
            (AppiumBy.ACCESSIBILITY_ID, "Cuidados diários"),
            (AppiumBy.ACCESSIBILITY_ID, "Conveniência"),
            (AppiumBy.ACCESSIBILITY_ID, "Mamãe e Bebê"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Ferramentas"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Ferramentas elétricas"),
            (AppiumBy.ACCESSIBILITY_ID, "ferramentas manuais"),
            (AppiumBy.ACCESSIBILITY_ID, "Material de construção"),
            (AppiumBy.ACCESSIBILITY_ID, "Jardinagem"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Festas e Eventos"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Eventos sociais"),
            (AppiumBy.ACCESSIBILITY_ID, "Eventos corporativos"),
            (AppiumBy.ACCESSIBILITY_ID, "Ferias"),
            (AppiumBy.ACCESSIBILITY_ID, "Eventos religiosos"),
            (AppiumBy.ACCESSIBILITY_ID, "Eventos acadêmicos e educacionais"),
            (AppiumBy.ACCESSIBILITY_ID, "Eventos culturais e de entretenimento"),
            (AppiumBy.ACCESSIBILITY_ID, "Eventos esportivos"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Fisioterapia"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Pilates"),
            (AppiumBy.ACCESSIBILITY_ID, "Reabilitação"),
            (AppiumBy.ACCESSIBILITY_ID, "Acupuntura"),
            (AppiumBy.ACCESSIBILITY_ID, "Fisioterapia Esportiva"),
            (AppiumBy.ACCESSIBILITY_ID, "Quiropaxia"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        time.sleep(1)
        app_scroll(self.driver)
        print('Fisioterapia')

        #
        category_value = "Fretes e Mudanças"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Fretes e mudanças de curta distancia"),
            (AppiumBy.ACCESSIBILITY_ID, "Fretes e mudanças interestaduais"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Funerária"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Velório"),
            (AppiumBy.ACCESSIBILITY_ID, "Cremação"),
            (AppiumBy.ACCESSIBILITY_ID, "Translados aérios e terrestres, em território nacional e ou internacional"),
            (AppiumBy.ACCESSIBILITY_ID, "Tratamentos Restauração facial, formolização, embalsamento, conservação por climatização e tanatopraxia."),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Guia Turístico"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Excursão nacional"),
            (AppiumBy.ACCESSIBILITY_ID, "Excurção internacional"),
            (AppiumBy.ACCESSIBILITY_ID, "Excurção regional"),
            (AppiumBy.ACCESSIBILITY_ID, "Especialista em atrativos turísticos"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        category_value = "Guincho"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Caminhão guincho de corrente e gancho"),
            (AppiumBy.ACCESSIBILITY_ID, "Caminhão guincho de plataforma"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Hospedagem"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Pousada"),
            (AppiumBy.ACCESSIBILITY_ID, "Hotel"),
            (AppiumBy.ACCESSIBILITY_ID, "Apartamento ou casa para temporada"),
            (AppiumBy.ACCESSIBILITY_ID, "Hostel"),
            (AppiumBy.ACCESSIBILITY_ID, "Apart-Hotels"),
            (AppiumBy.ACCESSIBILITY_ID, "Resorts"),
            (AppiumBy.ACCESSIBILITY_ID, "Hospedagem em acampamento"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Hospedagem e creche para Pets"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Hotéis para animais"),
            (AppiumBy.ACCESSIBILITY_ID, "Hotel domiciliar para pets"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        time.sleep(1)
        app_scroll(self.driver)
        print('Hospedagem e creche')

        #
        category_value = "Informática"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Hardware, Placa mãe, Processadores, GPUS"),
            (AppiumBy.ACCESSIBILITY_ID, "Software, licenças e Sistema Operacional"),
            (AppiumBy.ACCESSIBILITY_ID, "Armazenamento, HDs SSDs, Pendrive"),
            (AppiumBy.ACCESSIBILITY_ID, "Componentes de computadores, Memória e Fontes"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Instrumentos musicais"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Guitarras, Violões e Baixos"),
            (AppiumBy.ACCESSIBILITY_ID, "Som e Multimídia"),
            (AppiumBy.ACCESSIBILITY_ID, "Pianos, Telcados e Sintetizadores"),
            (AppiumBy.ACCESSIBILITY_ID, "Microfones, Mesas de som e Equipamentos de estúdio"),
            (AppiumBy.ACCESSIBILITY_ID, "BAterias e Percussão"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Jardineiro"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Jardinagem residencial e comercial"),
            (AppiumBy.ACCESSIBILITY_ID, "Manutenção de jardins"),
            (AppiumBy.ACCESSIBILITY_ID, "Consultoria Especializada"),
            (AppiumBy.ACCESSIBILITY_ID, "Paisagismo"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "joalheiro"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "limpeza de joias"),
            (AppiumBy.ACCESSIBILITY_ID, "conserto de fechos"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Joalheiro"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Criação, Fabricação, Ajustes e Reparos"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Limpeza pós obra"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "limpeza bruta: retirada de detritos pesados e eliminação de sujidades; limpeza técnica: remoção dos restos de obra e limpeza de vidros e esquadrias; limpeza final: higienização e organização detalhada do ambiente para uso."),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        #
        time.sleep(1)
        app_scroll(self.driver)
        print('Limpeza pós obra')
        
        #
        category_value = "livraria e papelaria"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "livros"),
            (AppiumBy.ACCESSIBILITY_ID, "lapis"),
            (AppiumBy.ACCESSIBILITY_ID, "canetas"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Manicure"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Manicure Tradicional"),
            (AppiumBy.ACCESSIBILITY_ID, "Unhas em Gel"),
            (AppiumBy.ACCESSIBILITY_ID, "Alongamento"),
            (AppiumBy.ACCESSIBILITY_ID, "Banho de parafina"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        time.sleep(1)
        app_scroll(self.driver)
        print('Manicure')

        #
        category_value = "Marceneiro"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Fabricação de móveis"),
            (AppiumBy.ACCESSIBILITY_ID, "Montagem"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Marido de aluguel"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Atendimento residencial de serviços gerais"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Massagista"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Massagem relaxante"),
            (AppiumBy.ACCESSIBILITY_ID, "Drenagem linfática"),
            (AppiumBy.ACCESSIBILITY_ID, "Massagem modeladora"),
            (AppiumBy.ACCESSIBILITY_ID, "Shiatsu"),
            (AppiumBy.ACCESSIBILITY_ID, "Massagem Tailandesa"),
            (AppiumBy.ACCESSIBILITY_ID, "Massagem Ayurvédica"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        
        category_value = "Material de construção"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Louças"),
            (AppiumBy.ACCESSIBILITY_ID, "acessórios"),
            (AppiumBy.ACCESSIBILITY_ID, "Cimento"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Mecânica"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Funilaria e Pintura"),
            (AppiumBy.ACCESSIBILITY_ID, "Manutenção Corretica Planejada"),
            (AppiumBy.ACCESSIBILITY_ID, "Troca de óleo"),
            (AppiumBy.ACCESSIBILITY_ID, "Alinhamento e balanceamento"),
            (AppiumBy.ACCESSIBILITY_ID, "Manutenção de embreagem"),
            (AppiumBy.ACCESSIBILITY_ID, "Revisão dos componentes de freio"),
            (AppiumBy.ACCESSIBILITY_ID, "Reparos de motor"),
            (AppiumBy.ACCESSIBILITY_ID, "Elétrica e eletrônica"),
            (AppiumBy.ACCESSIBILITY_ID, "Diagnóstico"),
            (AppiumBy.ACCESSIBILITY_ID, "Reparo de suspensão"),
            (AppiumBy.ACCESSIBILITY_ID, "Troca de bateria"),
            (AppiumBy.ACCESSIBILITY_ID, "Serviços de ar condicionado"),
            (AppiumBy.ACCESSIBILITY_ID, "Troca de fluidos e lubrificantes"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Mestres"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Mestres da Web"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        time.sleep(1)
        app_scroll(self.driver)
        print('Mestres')

        #
        category_value = "Moda"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Roupas Femininas"),
            (AppiumBy.ACCESSIBILITY_ID, "Roupas Masculinas"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Motorista"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Motorista particular"),
            (AppiumBy.ACCESSIBILITY_ID, "Motorista categoria D"),
            (AppiumBy.ACCESSIBILITY_ID, "Motorista categoria B"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Manutenção, Pilates e equipamento de treino"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Elásticos"),
            (AppiumBy.ACCESSIBILITY_ID, "Esteiras, Elípticos, Bicicletas Ergométricas"),
            (AppiumBy.ACCESSIBILITY_ID, "Estação de musculação"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Nutricionista"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Nutricionista clínica"),
            (AppiumBy.ACCESSIBILITY_ID, "Nutricionista esportiva"),
            (AppiumBy.ACCESSIBILITY_ID, "Nutrição Bariátrica"),
            (AppiumBy.ACCESSIBILITY_ID, "Nutrição Oncológica"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Pedreiro"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Pedreiro Geral"),
            (AppiumBy.ACCESSIBILITY_ID, "Pedreiro Azulejista"),
            (AppiumBy.ACCESSIBILITY_ID, "Pedreiro de Alvenaria"),
            (AppiumBy.ACCESSIBILITY_ID, "Pedreiro de Acabamento"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Personal Trainer"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Elaborar rotinas de treinamento"),
            (AppiumBy.ACCESSIBILITY_ID, "Fazer o acompanhamento físico"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        time.sleep(1)
        app_scroll(self.driver)
        print('Personal')

        #
        category_value = "Pet"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Rações e petiscos"),
            (AppiumBy.ACCESSIBILITY_ID, "Brinquedos Pet"),
            (AppiumBy.ACCESSIBILITY_ID, "Acessórios Pet"),
            (AppiumBy.ACCESSIBILITY_ID, "Higiene Pet"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Pintor"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Pintura em residências e comércios"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Professor(a) Particular"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Português"),
            (AppiumBy.ACCESSIBILITY_ID, "Matemática"),
            (AppiumBy.ACCESSIBILITY_ID, "Química"),
            (AppiumBy.ACCESSIBILITY_ID, "Física"),
            (AppiumBy.ACCESSIBILITY_ID, "Biologia"),
            (AppiumBy.ACCESSIBILITY_ID, "História"),
            (AppiumBy.ACCESSIBILITY_ID, "Geografia"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Restaurante"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Almoço"),
            (AppiumBy.ACCESSIBILITY_ID, "Jantar"),
            (AppiumBy.ACCESSIBILITY_ID, "Café da manhã"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Roupas Femininas"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Roupa feminina"),
            (AppiumBy.ACCESSIBILITY_ID, "Roupa masculina"),
            (AppiumBy.ACCESSIBILITY_ID, "Roupa infantil masculina"),
            (AppiumBy.ACCESSIBILITY_ID, "Roupa infantil feminina"),
            (AppiumBy.ACCESSIBILITY_ID, "Roupa de bebês"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Veículos"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Peças para Carro e Moto"),
            (AppiumBy.ACCESSIBILITY_ID, "Pneus e Rodas"),
            (AppiumBy.ACCESSIBILITY_ID, "Equipamentos de segurança"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)

        #
        category_value = "Veterinário"
        subcategory_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Atendimento 24h"),
            (AppiumBy.ACCESSIBILITY_ID, "Consulta"),
            (AppiumBy.ACCESSIBILITY_ID, "Vacinas"),
            (AppiumBy.ACCESSIBILITY_ID, "Exames de sangue"),
            (AppiumBy.ACCESSIBILITY_ID, "Exames de ultrassom e raio-x"),
            (AppiumBy.ACCESSIBILITY_ID, "Cirurgias"),
            (AppiumBy.ACCESSIBILITY_ID, "Internação"),
        ]
        select_category_and_subcategories(self, wait, category_locator, category_value, subcategory_locators)
        
        time.sleep(10)
              
if __name__ == '__main__':
    unittest.main()
    
    