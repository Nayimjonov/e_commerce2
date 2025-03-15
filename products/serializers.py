from rest_framework import serializers
from .models import Product
from categories.models import Category


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'category')


