from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from .models import Order
from .serializers import OrderSerializer


class OrderPagination(PageNumberPagination):
    page_size = 10


class OrderListCreateAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        paginator = OrderPagination()
        result_page = paginator.paginate_queryset(orders, request)

        serializer = OrderSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPIView(APIView):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
