from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import OrderSerializer
from .service import create_order


class OrderCreateAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            response = create_order(data=serializer.data)
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

