# Scraperfy
> A Brazilian financial market data web scraping package.


## Getting Started

To get a local copy of the Scraperfy package follow these steps.

### Prerequisites

* [Python 3.9](https://www.python.org/downloads/)
* [Selenium](https://selenium-python.readthedocs.io/index.html)

### Installation

Clone this repo into a directory:
```
git clone https://github.com/fredericoqueiroz/scraperfy.git
```

## Usage

It's recommended to install the package inside a virtual environment.

Create a virtual environment ([pipenv](https://pypi.org/project/pipenv/) recommended):
```sh
pipenv shell
```

Install the Scraperfy package from the directory path where the repo was previously cloned:
```sh
pip install -e <path>
```

Install [Selenium](https://selenium-python.readthedocs.io/index.html) package:
```sh
pip install selenium
```

In order to use the Scraperfy library, it is necessary to instantiate a webdriver for Selenium. Selenium requires a driver to interface with the chosen brower. Firefox, for example, requires [geckodriver](https://github.com/mozilla/geckodriver/releases).

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers.

| Browser | Download link |
|---------|---|
| Chrome  | [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)  |
| Edge    | [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) |
| Firefox | [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases) |
| Safari  | [https://webkit.org/blog/6900/webdriver-support-in-safari-10/](https://webkit.org/blog/6900/webdriver-support-in-safari-10/) |


For more information about driver installation, please refer the [official documentation](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).

## Modules Usage Examples

This section presents usage examples of the modules in the scraperfy package.

### [Company Indicators Module](https://github.com/fredericoqueiroz/scraperfy/blob/main/scraperfy/company_indicators/company_indicators.py)

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from scraperfy.company_indicators import company_indicators as ci

PATH = "C:/Program Files (x86)/geckodriver.exe"

op = Options()
op.add_argument('--headless')

driver = webdriver.Firefox(executable_path=PATH, options=op)

company = ci.CompanyIndicators(driver, 'AAPL', american=True)

print(company.get_profitability_indicators())
```

Result:

```json
(package-test) D:\GitHub\package-test>py company_indicator_example.py
{
    "RetornoPatrimonioLiquido": {
        "simbolo": "ROE",
        "valor": "110,31%",
        "descricao": "Mede a capacidade de agregar valor de uma empresa a partir de seus próprios recursos e do dinheiro de investidores."
    },
    "RetornoAtivo": {
        "simbolo": "ROA",
        "valor": "22,63%",
        "descricao": "O retorno sobre os ativos ou Return on Assets, é um indicador de rentabilidade, que calcula a capacidade de uma empresa gerar lucro a partir dos seus ativos, além de indiretamente, indicar a eficiência dos seus gestores."
    },
    "RetornoCapitalInvestido": {
        "simbolo": "ROIC",
        "valor": "39,99%",
        "descricao": "Mede a rentabilidade de dinheiro o que uma empresa é capaz de gerar em razão de todo o capital investido, incluindo os aportes por meio de dívidas."
    },
    "GiroAtivos": {
        "simbolo": "GIRO ATIVOS",
        "valor": "0,97",
        "descricao": "Mede se como uma empresa está utilizando o seu ativo (bens, investimentos, estoque etc.) para produzir riqueza, através da venda de seus produtos e/ou serviços."
    }
}
```

### [Intraday Asset Price Module](https://github.com/fredericoqueiroz/scraperfy/blob/main/scraperfy/intraday_scraper/current_price.py)

```python
from selenium import webdriver
from scraperfy.intraday_scraper import current_price as cp

PATH = "C:/Program Files (x86)/chromedriver.exe"

op = webdriver.ChromeOptions()
op.add_argument('headless')

driver = webdriver.Chrome(PATH, options=op)

asset = cp.CurrentPrice(driver, 'PETR4')

print(asset.get_json())
```

Result:

```json
{
   "ativo": "PETR4",
   "cotacaoAtivo": "28.25",
   "oscilacaoAtivo": "+0.42",
   "dataConsulta": "18/06/2021",
   "horaConsulta": "19:29"
}
```

### [Index Theoretical Daily Portifolio](https://github.com/fredericoqueiroz/scraperfy/blob/main/scraperfy/index_scraper/theoretical_portifolio.py)

```python
import json

from selenium import webdriver
from scraperfy.index_scraper import theoretical_portifolio as tp

PATH = "C:/Program Files (x86)/chromedriver.exe"

op = webdriver.ChromeOptions()
op.add_argument('headless')

driver = webdriver.Chrome(PATH, options=op)

index = tp.TheoreticalDailyPortifolio(driver, 'ibov')

ibov = index.get_json()
parsed = json.loads(ibov)
print(json.dumps(parsed, indent=4))
```
Result (peek):
```sh
{
    "ABEV3": {
        "nome": "AMBEV S/A",
        "tipo": "ON",
        "quantidadeTeorica": "4.358.542.894",
        "participacao": "3,514"
    },
    "ASAI3": {
        "nome": "ASSAI",
        "tipo": "ON NM",
        "quantidadeTeorica": "88.180.251",
        "participacao": "0,322"
    },
    "AZUL4": {
        "nome": "AZUL",
        "tipo": "PN N2",
        "quantidadeTeorica": "327.262.616",
        "participacao": "0,659"
    },
    "BTOW3": {
        "nome": "B2W DIGITAL",
        "tipo": "ON NM",
        "quantidadeTeorica": "201.802.882",
        "participacao": "0,611"
    },
    "B3SA3": {
        "nome": "B3",
        "tipo": "ON NM",
        "quantidadeTeorica": "6.119.434.194",
        "participacao": "4,571"
    },
    "BIDI11": {
        "nome": "BANCO INTER",
        "tipo": "UNT N2",
        "quantidadeTeorica": "235.350.939",
        "participacao": "0,688"
    },
    "BBSE3": {
        "nome": "BBSEGURIDADE",
        "tipo": "ON NM",
        "quantidadeTeorica": "671.584.841",
        "participacao": "0,732"
    },
    ...
}
Data do portifolio: 2021-06-21
Titulo do portifolio: Carteira do Dia - 21/06/21
Descricao do portifolio: Carteira Teórica do IBovespa válida para 21/06/21
```

## Contributing

Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/fredericoqueiroz/scraperfy/blob/main/LICENSE) for more information.