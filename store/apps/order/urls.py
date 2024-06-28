from django.urls import path
from apps.order.views import OrderCreateAPIView

urlpatterns = [
    path('orders', OrderCreateAPIView.as_view(), name='orders'),
]
