from django.urls import path
from .views import StockView


urlpatterns = [
    path(r'inventories/product/<int:product_id>', StockView.as_view(), name='inventory'),
]