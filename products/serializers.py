from rest_framework import serializers
from .models import Product
from categories.serializers import CategoryModelSerializer


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'category')

