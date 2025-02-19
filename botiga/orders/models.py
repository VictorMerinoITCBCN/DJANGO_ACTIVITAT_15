from django.db import models
from botiga.models import User

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