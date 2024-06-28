from rest_framework import serializers
from .custom_reponses import product_not_found, out_of_stock
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from apps.inventory.models import Stock


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, attrs):
        product_id = attrs['product_id']
        try:
            stock = Stock.objects.get(product_id=product_id)
        except ObjectDoesNotExist:
            raise product_not_found()

        if stock.quantity < attrs['quantity']:
            raise out_of_stock(
                sku=stock.product.sku,
                name=stock.product.name
            )

        return attrs


class OrderSerializer(serializers.Serializer):
    customer_email = serializers.CharField()
    customer_phone = serializers.CharField()
    customer_name = serializers.CharField()
    customer_address = serializers.CharField()
    items = OrderItemSerializer(many=True)

