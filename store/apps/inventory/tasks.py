import logging
from store.celery import app
from .models import Stock

logger = logging.getLogger("apps.inventory")


@app.task(bind=True, ignore_result=True)
def check_stock(self):
    logger.info("Looking for low stock.")
    for stock in Stock.objects.filter(quantity__lt=10):
        logger.warning(
            f"Product {stock.product.sku}/{stock.product.name} "
            f"has a low quantity stock: {stock.quantity}"
        )
