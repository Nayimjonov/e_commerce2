from rest_framework import serializers
from .models import Products
from categories.models import Categories


class ProductModelSerializer(serializers.ModelSerializer):
    category =  serializers.CharField()

    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price', 'stock', 'category')


