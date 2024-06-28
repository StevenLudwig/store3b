from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from apps.inventory.models import Stock
from .serializers import ProductModelSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.select_related('product')
    serializer_class = ProductModelSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        Stock.objects.create(product=product)
        serialized_product = ProductModelSerializer(product)
        return Response(serialized_product.data, status=HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        return Response([{
            'id': item_stock.product.id,
            'name': item_stock.product.name,
            'sku': item_stock.product.sku,
            'price': item_stock.product.price,
            'is_active': item_stock.product.is_active,
            'created_at': item_stock.product.created_at,
            'updated_at': item_stock.product.updated_at,
            'out_of_stock': item_stock.quantity == 0,
            'available_quantity': item_stock.quantity
        } for item_stock in self.queryset])
