from urllib.request import urlopen
import json
import requests
NOT_EXIST_ERROR = "Crypto with that name and currency does not exist in database"
EXTERNAL_API_ERROR = "External api did not send correct response"
NOT_EXIST_API_ERROR = "Crypto with that name and currency does not exist in external API"

#przeniesc do jakiegos serwisu

def get_new_crypto_price(self, name, currency_code):
    response = urlopen(self.crypto_url + '&ids=' + name + '&convert=' + currency_code)
    if response.status != 200:
        return EXTERNAL_API_ERROR #add logging later
    data_table = json.loads(response.read())
    if not data_table:
        return NOT_EXIST_API_ERROR #add logging later
    return float(data_table[0]['price'])

def get_new_metal_price(self, name, currency_code):
    name = name.lower()
    resp = requests.get(self.metal_url, verify=False)
    if resp.status_code != 200:
        return EXTERNAL_API_ERROR
    data_table = json.loads(resp.text)
    usd_price = 0
    for data in data_table:
        if data.get(name, '') != '':
            usd_price = data[name]
    currency_usd_ratio = getattr(Asset.objects.get(name='USD'), 'converter' + currency_code)
    return float(usd_price) * float(currency_usd_ratio)

def get_new_currency_price(self, name, currency_code):
    response = urlopen(self.currency_url.format(name, currency_code))
    if response.status != 200:
        return EXTERNAL_API_ERROR
    data_table = json.loads(response.read())
    if not data_table:
        return NOT_EXIST_API_ERROR
    return float(data_table['info']['rate'])

def update_asset_in_server(self, name):
    try:
        asset = Asset.objects.get(name=name)
    except Asset.DoesNotExist:
        return NOT_EXIST_ERROR
    json_data = {
        "id": asset.guidA,
        "type": asset.asset_type,
        "name": name,
        "converterPLN": asset.converterPLN,
        "converterEUR": asset.converterEUR,
        "converterUSD": asset.converterUSD
    }
    response = requests.put(self.server_url + asset.guidA, json=json_data, verify=False)
    return response

