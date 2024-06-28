import pytest
from rest_framework import status
from decimal import Decimal
from datetime import datetime
from django.utils import timezone
from rest_framework.test import APIClient

from apps.inventory.models import Stock
from apps.catalog.models import Product

PRODUCT_BASE_MOCK = {
    'name': 'Colchon',
    'sku': 'LU1001',
    'price': Decimal('7999.00'),
}
PRODUCT_BASE_MOCK2 = {
    'name': 'Colchon King',
    'sku': 'LU1004',
    'price': Decimal('18999.00'),
}

FULL_PRODUCT_MOCK = {
    **PRODUCT_BASE_MOCK,
    **{
        'is_active': True,
        'created_at': timezone.now(),
        'updated_at': timezone.now()
    }
}


def test_product_model():
    product = Product(**FULL_PRODUCT_MOCK)

    assert product.name == PRODUCT_BASE_MOCK['name']
    assert product.sku == PRODUCT_BASE_MOCK['sku']
    assert product.price == PRODUCT_BASE_MOCK['price']
    assert product.is_active is True
    assert isinstance(product.created_at, datetime)
    assert isinstance(product.updated_at, datetime)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_product(api_client):
    response = api_client.post('/api/products', PRODUCT_BASE_MOCK, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    product = Product.objects.get(sku=PRODUCT_BASE_MOCK['sku'])
    assert product.name == PRODUCT_BASE_MOCK['name']
    stock = Stock.objects.get(product__pk=product.id)
    assert stock.quantity == 100


@pytest.mark.django_db
def test_list_products(api_client):
    # Product 1
    product1 = Product.objects.create(**PRODUCT_BASE_MOCK)
    Stock.objects.create(product=product1)
    # Product 2
    product2 = Product.objects.create(**PRODUCT_BASE_MOCK2)
    Stock.objects.create(product=product2)
    response = api_client.get('/api/products')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['name'] == PRODUCT_BASE_MOCK['name']
    assert response.data[0]['available_quantity'] == 100
    assert response.data[1]['name'] == PRODUCT_BASE_MOCK2['name']
    assert response.data[1]['available_quantity'] == 100
