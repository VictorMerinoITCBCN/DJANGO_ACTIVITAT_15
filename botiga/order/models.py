from django.db import models
from botiga.models import User

class StatusChoices(models.TextChoices):
    PENDING = "PENDING", "Pending"
    PAID = "PAID", "Paid"
    SHIPPED = "SHIPPED", "Shipped"
    DELIVERED = "DELIVERED", "Delivered"
    CANCELLED = "CANCELLED", "Cancelled"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=StatusChoices, default=StatusChoices.PENDING)

    @property
    def total_price(self):
        return sum(item.product.price * item.product.quantity for item in self.orderitem_set.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()