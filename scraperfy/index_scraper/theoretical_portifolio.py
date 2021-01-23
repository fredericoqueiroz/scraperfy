#from selenium import webdriver
import pandas as pd

pd.set_option('display.min_rows', 50)
pd.set_option('display.max.rows', 200)

class TheoreticalPortifolio:
    def __init__(self, driver, index):
        self.driver = driver
        self.url = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice={}&idioma=pt-br'.format(index.upper())
        self.table = pd.DataFrame()
        self.table_index = ['codigo', 'acao', 'tipo', 'quantidadeTeorica', 'participacao']

    def navigate(self):
        self.driver.get(self.url)

    def get_table(self):
        self.table = pd.read_html(self.url, decimal=',', thousands='.')[0][:-1]
        self.table.columns = self.table_index
        self.table.set_index(self.table_index[0], inplace=True)

    def get_json(self):
        return self.table.to_json(orient="index")

    def print_table(self):
        print(self.table)
