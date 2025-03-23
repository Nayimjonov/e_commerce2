from rest_framework import serializers
from .models import OrderItem, Order
from products.models import Product
from products.serializers import ProductModelSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = OrderItem
        fields = ('product', 'product_id', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='order_items', many=True)
    status = serializers.CharField(default="processing", read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'customer_name',
            'customer_email',
            'customer_phone',
            'items',
            'total_price',
            'status',
            'created_at',
        )

    def create(self, validated_data):
        items_data = validated_data.pop('order_items', [])
        order = Order.objects.create(**validated_data)
        total_price = 0

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price * quantity
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
            total_price += price

        order.total_price = total_price
        order.save()
        return order
