from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.driver.implicitly_wait(30)
        self.driver.get(self.url)

    def _search_asset(self):
        self.driver.find_element_by_id(self.search_input_id).send_keys(self.asset)
        self.driver.find_element_by_id(self.search_button_id).click()

    def _scrape_asset_data(self):
        self.search_date = self.driver.find_element_by_id('dataConsulta').text
        self.search_time = self.driver.find_element_by_id('horaConsulta').text
        self.asset_symbol = self.driver.find_element_by_id('ativo').text
        self.asset_price = self.driver.find_element_by_id('cotacaoAtivo').text
        self.asset_oscilation = self.driver.find_element_by_id('oscilacaoAtivo').text

    def get_search_date(self):
        return self.search_date

    #debug
    def print_asset_data(self):
        print(f'Data da Consulta: {self.search_date}')
        print(f'Hora da Consulta: {self.search_time}')
        print(f'Ativo: {self.asset_symbol}')
        print(f'Cotacao: {self.asset_price}')
        print(f'Oscilacao: {self.asset_oscilation}')