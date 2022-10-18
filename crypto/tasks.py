from celery import shared_task
from crypto.updater_service import PriceUpdater


@shared_task()
def update_asset_price_on_server(name):
    PriceUpdater().update_asset_in_server(name)
