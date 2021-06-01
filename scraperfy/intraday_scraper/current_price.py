import datetime
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CurrentPrice:
    def __init__(self, driver, asset):
        self.driver = driver
        self.asset = asset.upper()
        self.url = 'http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/outros-ativos.htm'
        self.search_input_id = 'txtCampoPesquisa'
        self.search_button_id = 'btnBuscarOutrosAtivos'
        self.search_date = ''
        self.search_time = ''
        self.asset_symbol = ''
        self.asset_price = ''
        self.asset_oscilation = ''

        self._navigate()
        self._search_asset()
        self._scrape_asset_data()

    def _navigate(self):
        self.driver.get(self.url)

    def _search_asset(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.element_to_be_clickable((By.ID, self.search_button_id)),
            message=f'Failed to fetch asset {self.asset}'
        )
        self.driver.find_element_by_id(self.search_input_id).send_keys(self.asset)
        self.driver.find_element_by_id(self.search_button_id).click()

    def _scrape_asset_data(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(
            EC.text_to_be_present_in_element(
                (By.ID, 'ativo'), 
                '______',
            ),
            message=f'Failed to fetch asset {self.asset}'
        )
        self.search_date = self.driver.find_element_by_id('dataConsulta').text
        self.search_time = self.driver.find_element_by_id('horaConsulta').text
        self.asset_symbol = self.driver.find_element_by_id('ativo').text
        self.asset_price = self.driver.find_element_by_id('cotacaoAtivo').text
        self.asset_oscilation = self.driver.find_element_by_id('oscilacaoAtivo').text

    def get_asset_symbol(self):
        return self.asset_symbol
    
    def get_asset_price(self):
        return self.asset_price
    
    def get_asset_oscilation(self):
        return self.asset_oscilation
    
    def get_search_date(self):
        d, m, y = self.search_date.split('/')
        search_date = datetime.date(int(y), int(m), int(d))
        return search_date

    def get_search_time(self):
        return self.search_time
    
    def get_json(self):
        dict = {
            'ativo': self.asset_symbol,
            'cotacaoAtivo': self.asset_price,
            'oscilacaoAtivo': self.asset_oscilation,
            'dataConsulta': self.search_date,
            'horaConsulta': self.search_time
        }
        return json.dumps(dict, sort_keys=False, indent=3)

    '''Debug'''
    def print_asset_data(self):
        print(f'Data da Consulta: {self.search_date}')
        print(f'Hora da Consulta: {self.search_time}')
        print(f'Ativo: {self.asset_symbol}')
        print(f'Cotacao: {self.asset_price}')
        print(f'Oscilacao: {self.asset_oscilation}')
