from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Stock
from .serializers import StockSerializer


class StockView(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, product_id):
        try:
            return Stock.objects.get(product__pk=product_id)
        except Stock.DoesNotExist:
            return None

    def patch(self, request, product_id):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            stock = self.get_object(product_id=product_id)
            if not stock:
                return Response(
                    data={'error': 'Product not found'},
                    status=status.HTTP_404_NOT_FOUND
                )

            stock.quantity = data['quantity']
            stock.save()
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



