from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'grand_total',
        'customer_email',
        'customer_phone',
        'customer_name',
        'customer_address',
        'created_at',
    )
    search_fields = ('order_number',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'name',
        'sku',
        'quantity',
        'price',
        'is_active',
        'created_at',
    )
    search_fields = ('sku',)
