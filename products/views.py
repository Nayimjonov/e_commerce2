from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from serializers import ProductModelSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def product_list(request, pk=None):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        product = get_object_or_404(Products, pk=pk)
        serializer = ProductModelSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product = get_object_or_404(Products, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
