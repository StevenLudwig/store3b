from typing import List
from decimal import Decimal
from pydantic import BaseModel

from apps.inventory.models import Stock
from .helpers import generate_order_number
from .models import Order, OrderItem


class OrderItemResponse(BaseModel):
    name: str
    sku: str
    quantity: int
    price: Decimal


class OrderResponse(BaseModel):
    order_number: str
    grand_total: Decimal = 0
    customer_email: str
    customer_name: str
    customer_phone: str
    customer_address: str
    items: List[OrderItemResponse | None] = []


def create_order(data: dict):
    grand_total: Decimal = Decimal('0.00')
    order_items = []
    order_response = OrderResponse(
        order_number=generate_order_number(),
        customer_email=data['customer_email'],
        customer_name=data['customer_name'],
        customer_phone=data['customer_phone'],
        customer_address=data['customer_address'],
    )

    for item in data['items']:
        quantity = item.get('quantity')
        stock = Stock.objects.get(product__pk=item.get('product_id'))
        order_items.append(OrderItemResponse(
            name=stock.product.name,
            sku=stock.product.sku,
            quantity=quantity,
            price=stock.product.price
        ))
        grand_total += stock.product.price * quantity
        stock.quantity = abs(stock.quantity - quantity)
        stock.save()

    order_response.grand_total = grand_total
    order = Order.objects.create(**order_response.model_dump(exclude={'items'}))

    for item in order_items:
        OrderItem.objects.create(order=order, **item.model_dump())
    order_response.items = order_items

    return order_response.model_dump()
