from urllib.request import urlopen
import json
import requests
import logging
from datetime import datetime, timedelta

NOT_EXIST_ERROR = "Crypto with that name and currency does not exist in database"
EXTERNAL_API_ERROR = "External api did not send correct response"
NOT_EXIST_API_ERROR = "Crypto with that name and currency does not exist in external API"
SERVER_URL = 'http://host.docker.internal:5000/api/asset-values/{}'


class PriceUpdater:
    crypto_url = 'https://api.coingecko.com/api/v3/simple/price'
    metal_url = 'https://api.metals.live/v1/spot'
    currency_url = 'https://api.exchangerate.host/convert?from={}&to={}'
    currencies = ['eur', 'pln', 'jpy', 'gbp', 'huf', 'try', 'sek', 'chf', 'rub', 'nok', 'cad', 'inr', 'czk', 'hrk']
    metals = ['gold', 'silver', 'platinum']
    cryptos = ['btc', 'eth', 'ltc']
    Errors = [NOT_EXIST_ERROR, EXTERNAL_API_ERROR, NOT_EXIST_API_ERROR]
    logger = logging.getLogger(__name__)
    crypto_mapper = {
        'btc': 'bitcoin',
        'eth': 'ethereum',
        'ltc': 'litecoin'
    }

    @staticmethod
    def get_current_date():
        timestamp = str(datetime.now())
        timestamp = timestamp.replace(' ', 'T')
        timestamp += "+00:00"
        return str(timestamp)

    def get_new_crypto_price(self, name, currency_code='USD'):
        name = self.crypto_mapper.get(name, '')
        response = urlopen(self.crypto_url + '?ids=' + name + '&vs_currencies=' + currency_code)
        if response.status != 200:
            return EXTERNAL_API_ERROR
        data_table = json.loads(response.read())
        if not data_table:
            return NOT_EXIST_API_ERROR
        return float(data_table[name][currency_code.lower()])

    def get_new_metal_price(self, name):
        name = name.lower()
        resp = requests.get(self.metal_url, verify=False)
        if resp.status_code != 200:
            return EXTERNAL_API_ERROR
        data_table = json.loads(resp.text)
        usd_price = 0
        for data in data_table:
            if data.get(name, '') != '':
                usd_price = data[name]
        return float(usd_price)

    def get_new_currency_price(self, name, currency_code='USD'):
        response = urlopen(self.currency_url.format(name, currency_code))
        if response.status != 200:
            return EXTERNAL_API_ERROR
        data_table = json.loads(response.read())
        if not data_table:
            return NOT_EXIST_API_ERROR
        return float(data_table['info']['rate'])

    def get_asset_price(self, name):
        if name in self.cryptos:
            return self.get_new_crypto_price(name)
        if name in self.currencies:
            return self.get_new_currency_price(name)
        if name in self.metals:
            return self.get_new_metal_price(name)
        return NOT_EXIST_ERROR

    def update_asset_in_server(self, name):
        result = self.get_asset_price(name)
        if result in self.Errors:
            self.logger.debug(f"An Error occured: {result}")
            return result
        price = result
        timestamp = self.get_current_date()
        json_data = {
            'value': price,
            'timeStamp': timestamp
        }
        print(json_data)
        #print(self.get_current_date())
        response = requests.post(SERVER_URL.format(name), json=json_data, verify=False)
        #self.logger.debug(f"price of {name} was updated on {timestamp}, with new value {price}")
        return response.content
