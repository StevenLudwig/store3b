import pytest
from rest_framework import status

from apps.inventory.models import Stock
from apps.catalog.models import Product
from apps.catalog.tests import PRODUCT_BASE_MOCK, PRODUCT_BASE_MOCK2, api_client

ORDER_MOCK = {
    "customer_email": "steve@mail.com",
    "customer_phone": "5548937659",
    "customer_name": "Steve Beltran",
    "customer_address": "Cuernavaca, Morelos. CP 62790",
    "items": []
}


@pytest.mark.django_db
def test_create_order(api_client):
    response_product_1 = api_client.post('/api/products', PRODUCT_BASE_MOCK, format='json')
    assert response_product_1.status_code == status.HTTP_201_CREATED
    response_product_2 = api_client.post('/api/products', PRODUCT_BASE_MOCK2, format='json')
    assert response_product_2.status_code == status.HTTP_201_CREATED

    product1 = Product.objects.get(sku=PRODUCT_BASE_MOCK['sku'])
    grand_total_product1 = product1.price * 2
    product2 = Product.objects.get(sku=PRODUCT_BASE_MOCK2['sku'])
    grand_total_product2 = product2.price * 2
    grand_total = grand_total_product1 + grand_total_product2

    ORDER_MOCK['items'] = [
        {
            "product_id": product1.id,
            "quantity": 2
        },
        {
            "product_id": product2.id,
            "quantity": 2
        }
    ]

    order_response = api_client.post('/api/orders', ORDER_MOCK, format='json')

    assert order_response.status_code == status.HTTP_201_CREATED
    assert order_response.data['grand_total'] == grand_total
    assert len(order_response.data['items']) == 2

    stock1 = Stock.objects.get(product__pk=product1.id)
    assert stock1.quantity == 98

    stock2 = Stock.objects.get(product__pk=product2.id)
    assert stock2.quantity == 98
