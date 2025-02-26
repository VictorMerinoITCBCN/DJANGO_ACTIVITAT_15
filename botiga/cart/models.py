from django.db import models
from botiga.models import User

class Cart(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()