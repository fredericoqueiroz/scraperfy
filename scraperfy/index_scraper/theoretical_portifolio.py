import pandas as pd
from datetime import date

pd.set_option('display.min_rows', 50)
pd.set_option('display.max.rows', 200)

class TheoreticalDailyPortifolio:
    def __init__(self, driver, index):
        self.driver = driver
        self.url = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice={}&idioma=pt-br'.format(index.upper())
        self.portifolio_date = ""
        self.table = pd.DataFrame()
        self.table_index = ['codigo', 'nome', 'tipo', 'quantidadeTeorica', 'participacao']
        self.table_title = ""
        self.table_description = ""

        self._navigate()
        self._scrape_table_data()
        self._format_portifolio_date()

    def _navigate(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)

    def _scrape_table_data(self):
        self.table = pd.read_html(self.url, decimal=',', thousands='.')[0][:-1]
        self.table.columns = self.table_index
        self.table.set_index(self.table_index[0], inplace=True)
        
        self.table_title = self.driver.find_element_by_id("ctl00_contentPlaceHolderConteudo_lblTitulo").text
        self.table_description = self.driver.find_element_by_id("ctl00_contentPlaceHolderConteudo_lblAvisoTabela").text

    def _format_portifolio_date(self):
        day_month_year_list = (self.table_title.split(' ')[-1]).split('/')
        day_month_year_list[2] = f'20{day_month_year_list[2]}'
        d = date(int(day_month_year_list[2]), int(day_month_year_list[1]), int(day_month_year_list[0]))
        self.portifolio_date = d.isoformat()
        #self.portifolio_date = d.strftime('%Y%m%d')

    def get_data_frame(self):
        return self.table

    def get_json(self):
        return self.table.to_json(orient="index")
    
    def get_portifolio_date(self):
        return self.portifolio_date
    
    def get_title(self):
        return self.table_title
    
    def get_description(self):
        return self.table_description

