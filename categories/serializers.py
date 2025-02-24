from rest_framework import serializers


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categ