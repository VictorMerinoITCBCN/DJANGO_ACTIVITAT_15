from rest_framework import serializers
from django.utils.translation.trans_real import catalog

class ProductSerializer(serializers.Serializer):
    model = catalog
    fields = "__all__"