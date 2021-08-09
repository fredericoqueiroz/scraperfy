import json
from datetime import datetime

class CompanyIndicators:

    def __init__(self, driver, asset, american=False):

        self.driver = driver
        self.asset = asset.upper()
        self.url = f'https://statusinvest.com.br/acoes/eua/{self.asset}' if american else f'https://statusinvest.com.br/acoes/{self.asset}'
        self.search_date = datetime.now()
        self.valuation_indicators = {}
        self.debt_indicators = {}
        self.efficiency_indicators = {}
        self.profitability_indicators = {}
        self.growth_indicators = {}

        self._navigate()
        self._scrape_valuation_indicators()
        self._scrape_debt_indicators()
        self._scrape_efficiency_indicators()
        self._scrape_profitability_indicators()
        self._scrape_growth_indicators()

    def _navigate(self):

        self.driver.implicitly_wait(5)
        self.driver.get(self.url)

    def _scrape_single_indicator(self, base_element):

        base = base_element.find_element_by_xpath('.//div')

        data = {}
        data['simbolo'] = base.find_element_by_xpath('.//h3').text
        data['valor'] = base.find_element_by_xpath('.//div/strong').text
        data['descricao'] = base.get_attribute('title')

        return data

    def _scrape_valuation_indicators(self):

        group_element = self.driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[1]/div')

        # Dividend Yield
        dividend_yield = group_element.find_element_by_xpath('.//div[1]')
        self.valuation_indicators['DividendYield'] = self._scrape_single_indicator(dividend_yield)
        self.valuation_indicators['DividendYield']['valor'] = self.valuation_indicators['DividendYield']['valor'].replace('%', '')

        # Preco/Lucro
        price_earnings = group_element.find_element_by_xpath('.//div[2]')
        self.valuation_indicators['PrecoLucro'] = self._scrape_single_indicator(price_earnings)

        # Peg Ratio
        peg_ratio = group_element.find_element_by_xpath('.//div[3]')
        self.valuation_indicators['PegRatio'] = self._scrape_single_indicator(peg_ratio)

        # Preco/ValorPatrimonial
        price_book_value = group_element.find_element_by_xpath('.//div[4]')
        self.valuation_indicators['PrecoValorPatrimonial'] = self._scrape_single_indicator(price_book_value)

        # EnterpiseValue/EBITDA
        ev_ebitda = group_element.find_element_by_xpath('.//div[5]')
        self.valuation_indicators['EvEbitda'] = self._scrape_single_indicator(ev_ebitda)

        # EnterpiseValue/EBIT
        ev_ebit = group_element.find_element_by_xpath('.//div[6]')
        self.valuation_indicators['EvEbit'] = self._scrape_single_indicator(ev_ebit)

        # Preco/EBITDA
        price_ebitda = group_element.find_element_by_xpath('.//div[7]')
        self.valuation_indicators['PrecoEbitda'] = self._scrape_single_indicator(price_ebitda)

        # Preco/EBIT
        price_ebit = group_element.find_element_by_xpath('.//div[8]')
        self.valuation_indicators['PrecoEbit'] = self._scrape_single_indicator(price_ebit)

        # ValorPatrimonial/Acao
        book_value_share = group_element.find_element_by_xpath('.//div[9]')
        self.valuation_indicators['ValorPatrimonialAcao'] = self._scrape_single_indicator(book_value_share)

        # Preco/Ativo
        price_asset = group_element.find_element_by_xpath('.//div[10]')
        self.valuation_indicators['PrecoAtivo'] = self._scrape_single_indicator(price_asset)

        # Lucro/Acao
        earnings_share = group_element.find_element_by_xpath('.//div[11]')
        self.valuation_indicators['LucroAcao'] = self._scrape_single_indicator(earnings_share)

        # Preco/ReceitaLiquida
        prices_sales_ratio = group_element.find_element_by_xpath('.//div[12]')
        self.valuation_indicators['PrecoReceitaLiquida'] = self._scrape_single_indicator(prices_sales_ratio)

        # Preco/CapitalDeGiro
        prices_working_capital = group_element.find_element_by_xpath('.//div[13]')
        self.valuation_indicators['PrecoCapitalGiro'] = self._scrape_single_indicator(prices_working_capital)

        # Preco/AtivoCirculanteLiquido
        price_net_current_assets = group_element.find_element_by_xpath('.//div[14]')
        self.valuation_indicators['PrecoAtivoCirculanteLiquido'] = self._scrape_single_indicator(price_net_current_assets)

    def _scrape_debt_indicators(self):

        group_element = self.driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[2]/div')
        
        # DividaLiquida/PatrimonioLiquido
        debt_net_worth = group_element.find_element_by_xpath('.//div[1]')
        self.debt_indicators['DividaLiquidaPatrimonioLiquido'] = self._scrape_single_indicator(debt_net_worth)

        # DividaLiquida/EBITDA
        debt_ebitda = group_element.find_element_by_xpath('.//div[2]')
        self.debt_indicators['DividaLiquidaEbitda'] = self._scrape_single_indicator(debt_ebitda)

        # DividaLiquida/EBIT
        debt_ebit = group_element.find_element_by_xpath('.//div[3]')
        self.debt_indicators['DividaLiquidaEbit'] = self._scrape_single_indicator(debt_ebit)

        # PatrimonioLiquido/Ativos
        net_worth_assets = group_element.find_element_by_xpath('.//div[4]')
        self.debt_indicators['PatrimonioLiquidoAtivos'] = self._scrape_single_indicator(net_worth_assets)

        # Passivos/Ativos
        liabilities_assets = group_element.find_element_by_xpath('.//div[5]')
        self.debt_indicators['PassivosAtivos'] = self._scrape_single_indicator(liabilities_assets)

        # Liquidez Corrente
        current_liquidity = group_element.find_element_by_xpath('.//div[6]')
        self.debt_indicators['LiquidezCorrente'] = self._scrape_single_indicator(current_liquidity)

    def _scrape_efficiency_indicators(self):

        group_element = self.driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[3]/div')

        # Margem Bruta
        gross_margin = group_element.find_element_by_xpath('.//div[1]')
        self.efficiency_indicators['MargemBruta'] = self._scrape_single_indicator(gross_margin)

        # Margem EBITDA
        ebitda_margin = group_element.find_element_by_xpath('.//div[2]')
        self.efficiency_indicators['MargemEbitda'] = self._scrape_single_indicator(ebitda_margin)

        # Margem EBIT
        ebit_margin = group_element.find_element_by_xpath('.//div[3]')
        self.efficiency_indicators['MargemEbit'] = self._scrape_single_indicator(ebit_margin)

        # Margem Liquida
        net_margin = group_element.find_element_by_xpath('.//div[4]')
        self.efficiency_indicators['MargemLiquida'] = self._scrape_single_indicator(net_margin)

    def _scrape_profitability_indicators(self):

        group_element = self.driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[4]/div')

        # Retorno sobre Patrimonio Liquido (ROE)
        return_on_requity = group_element.find_element_by_xpath('.//div[1]')
        self.profitability_indicators['RetornoPatrimonioLiquido'] = self._scrape_single_indicator(return_on_requity)

        # Retorno sobre Ativo (ROA)
        return_on_assets = group_element.find_element_by_xpath('.//div[2]')
        self.profitability_indicators['RetornoAtivo'] = self._scrape_single_indicator(return_on_assets)

        # Retorno sobre Capital Investido (ROIC)
        return_on_invested_capital = group_element.find_element_by_xpath('.//div[3]')
        self.profitability_indicators['RetornoCapitalInvestido'] = self._scrape_single_indicator(return_on_invested_capital)

        # Giro Ativos
        asset_turnover_ratio = group_element.find_element_by_xpath('.//div[4]')
        self.profitability_indicators['GiroAtivos'] = self._scrape_single_indicator(asset_turnover_ratio)

    def _scrape_growth_indicators(self):

        group_element = self.driver.find_element_by_xpath('//*[@id="indicators-section"]/div[2]/div/div[5]/div')

        # CAGR Receita (Cinco anos)
        cagr_revenue = group_element.find_element_by_xpath('.//div[1]')
        self.growth_indicators['CagrReceitas'] = self._scrape_single_indicator(cagr_revenue)

        # CAGR Lucro (Cinco anos)
        cagr_profit = group_element.find_element_by_xpath('.//div[2]')
        self.growth_indicators['CagrLucros'] = self._scrape_single_indicator(cagr_profit)

    def get_asset(self):
        return self.asset
    
    def get_search_date(self):
        return self.search_date.isoformat()

    def get_valuation_indicators(self):

        return json.dumps(self.valuation_indicators, indent=4, ensure_ascii=False)

    def get_debt_indicators(self):

        return json.dumps(self.debt_indicators, indent=4, ensure_ascii=False)

    def get_efficiency_indicators(self):

        return json.dumps(self.efficiency_indicators, indent=4, ensure_ascii=False)
    
    def get_profitability_indicators(self):

        return json.dumps(self.profitability_indicators, indent=4, ensure_ascii=False)
    
    def get_growth_indicators(self):

        return json.dumps(self.growth_indicators, indent=4, ensure_ascii=False)

    def get_all_indicators(self):

        data = {}
        data['IndicadoresValuation'] = self.valuation_indicators
        data['IndicadoresEndividamento'] = self.debt_indicators
        data['IndicadoresEficiencia'] = self.efficiency_indicators
        data['IndicadoresRentabilidade'] = self.profitability_indicators
        data['IndicadoresCrescimento'] = self.growth_indicators

        return json.dumps(data, indent=4, ensure_ascii=False)
