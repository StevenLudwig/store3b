import pytest
from rest_framework import status

from apps.inventory.models import Stock
from apps.catalog.models import Product
from apps.catalog.tests import PRODUCT_BASE_MOCK, api_client


@pytest.mark.django_db
def test_create_stock(api_client):
    response = api_client.post('/api/products', PRODUCT_BASE_MOCK, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    stock = Stock.objects.get(product__sku=PRODUCT_BASE_MOCK['sku'])
    assert stock.quantity == 100


@pytest.mark.django_db
def test_update_stock(api_client):
    product = Product.objects.create(**PRODUCT_BASE_MOCK)
    stock = Stock.objects.create(product=product)
    assert stock.quantity == 100
    response = api_client.patch(
        f'/api/inventories/product/{product.id}',
        {'quantity': 10},
        format='json'
    )
    assert response.status_code == status.HTTP_200_OK
    stock_updated = Stock.objects.get(product__id=product.id)
    assert stock_updated.quantity == 10
