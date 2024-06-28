from rest_framework import serializers


class StockSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
