from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=32)
    grand_total = models.DecimalField(max_digits=7, decimal_places=2)
    customer_email = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=150)
    customer_address = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_number}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=80)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Item {self.name} for Order {self.order.order_number}"
