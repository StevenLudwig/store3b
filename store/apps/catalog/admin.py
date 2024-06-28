from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'is_active', 'created_at', 'updated_at',)
    search_fields = ('sku',)
