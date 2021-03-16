from datetime import date

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

pd.set_option('display.min_rows', 50)
pd.set_option('display.max.rows', 200)

class TheoreticalDailyPortifolio:

    def __init__(self, driver, index):

        self.driver = driver
        self.index = index.upper()
        self.url = f'https://sistemaswebb3-listados.b3.com.br/indexPage/day/{self.index}?language=pt-br'
        self.portifolio_size = 0
        self.portifolio_date = ""
        self.table = None
        self.table_index = ['codigo', 'nome', 'tipo', 'quantidadeTeorica', 'participacao']
        self.table_title = ""
        self.table_description = ""

        self._navigate()
        self._scrape_table_data()
        self._format_portifolio_date()

    def _navigate(self):

        self.driver.implicitly_wait(30)
        self.driver.get(self.url)

    def _expand_table(self):

        select_option = self.driver.find_element_by_xpath('//*[@id="selectPage"]/option[4]')
        select_option.click()

    def _scrape_table_data(self):

        self._expand_table()
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="listing_pagination"]/pagination-template/ul/li[4]/a')
            ),
            message=f'Failed to expand table',
        )

        self.portifolio_size = len(self.driver.find_elements_by_xpath('//*[@id="divContainerIframeB3"]/div/div[1]/form/div[2]/div/table/tbody/tr'))
        
        table_data = self.driver.find_element_by_xpath('//*[@id="divContainerIframeB3"]/div/div[1]/form/div[2]/div/table/tbody')

        data = []
        for row in table_data.find_elements_by_xpath('.//tr'):
            data.append((td.text for td in row.find_elements_by_xpath('.//td')))

        self.table = pd.DataFrame(data, columns=self.table_index)

        self.table.set_index(self.table_index[0], inplace=True)

        self.table_title = self.driver.find_element_by_xpath('//*[@id="divContainerIframeB3"]/div/div[1]/form/h2').text

        self.table_description = self.driver.find_element_by_xpath('//*[@id="divContainerIframeB3"]/div/div[1]/form/p').text

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

    def get_portifolio_size(self):
        return self.portifolio_size
    
    def get_title(self):
        return self.table_title
    
    def get_description(self):
        return self.table_description

