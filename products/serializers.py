from rest_framework import serializers
from .models import Products


class ProductModelSerializer(serializers.ModelSerializer):
    category =  serializers.StringRelatedField()

    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price', 'stock', 'category')
