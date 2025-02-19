from django.db import models

class StatusChoices(models.TextChoices):
    PENDING = "PENDING", "Pending"
    PAID = "PAID", "Paid"
    SHIPPED = "SHIPPED", "Shipped"
    DELIVERED = "DELIVERED", "Delivered"
    CANCELLED = "CANCELLED", "Cancelled"

class Cart(models.Model):
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    user = models.ForeignKey(User)
    status = models.CharField(choices=StatusChoices, default=StatusChoices.PENDING)

    @property
    def total_price(self):
        return sum(item.product.price for item in self.orderitem_set.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()