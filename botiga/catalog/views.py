from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializer import CatalegSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CatalegSerializer