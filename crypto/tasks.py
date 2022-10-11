from celery import shared_task
from crypto.models.Asset import Asset

asset = Asset()


@shared_task
def update_bitcoin_price_usd():
    asset.update_asset_price('BTC', 'USD')


@shared_task
def update_bitcoin_price_pln():
    asset.update_asset_price('BTC', 'PLN')


@shared_task
def update_bitcoin_price_eur():
    asset.update_asset_price('BTC', 'EUR')


@shared_task
def update_bitcoin_price_on_server():
    asset.update_asset_in_server('BTC')


@shared_task
def update_eth_price_usd():
    asset.update_asset_price('ETH', 'USD')


@shared_task
def update_eth_price_pln():
    asset.update_asset_price('ETH', 'PLN')


@shared_task
def update_eth_price_eur():
    asset.update_asset_price('ETH', 'EUR')


@shared_task
def update_eth_price_on_server():
    asset.update_asset_in_server('ETH')


@shared_task
def update_pln_price_usd():
    asset.update_asset_price('PLN', 'USD')


@shared_task
def update_pln_price_eur():
    asset.update_asset_price('PLN', 'EUR')


@shared_task
def update_pln_price_on_server():
    asset.update_asset_in_server('PLN')


@shared_task
def update_eur_price_usd():
    asset.update_asset_price('EUR', 'USD')


@shared_task
def update_eur_price_pln():
    asset.update_asset_price('EUR', 'PLN')


@shared_task
def update_eur_price_on_server():
    asset.update_asset_in_server('EUR')


@shared_task
def update_usd_price_eur():
    asset.update_asset_price('USD', 'EUR')


@shared_task
def update_usd_price_pln():
    asset.update_asset_price('USD', 'PLN')


@shared_task
def update_usd_price_on_server():
    asset.update_asset_in_server('USD')


@shared_task
def update_gbp_price_usd():
    asset.update_asset_price('GBP', 'USD')


@shared_task
def update_gbp_price_pln():
    asset.update_asset_price('GBP', 'PLN')


@shared_task
def update_gbp_price_eur():
    asset.update_asset_price('GBP', 'EUR')


@shared_task
def update_gbp_price_on_server():
    asset.update_asset_in_server('GBP')


@shared_task
def update_gold_price_usd():
    asset.update_asset_price('GOLD', 'USD')


@shared_task
def update_gold_price_pln():
    asset.update_asset_price('GOLD', 'PLN')


@shared_task
def update_gold_price_eur():
    asset.update_asset_price('GOLD', 'EUR')


@shared_task
def update_gold_price_on_server():
    asset.update_asset_in_server('GOLD')


@shared_task
def update_silver_price_usd():
    asset.update_asset_price('SILVER', 'USD')


@shared_task
def update_silver_price_pln():
    asset.update_asset_price('SILVER', 'PLN')


@shared_task
def update_silver_price_eur():
    asset.update_asset_price('SILVER', 'EUR')


@shared_task
def update_silver_price_on_server():
    asset.update_asset_in_server('SILVER')


