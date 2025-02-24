from rest_framework import serializers

from categories.models import Categories


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name', 'description')
