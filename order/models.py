from django.db import models
from product.models import Product

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.quantity}x {self.product.name}"
