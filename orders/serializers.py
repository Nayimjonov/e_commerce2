from rest_framework import serializers
from .models import OrderItem, Order
from products.models import Product


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = OrderItem
        fields = ('product', 'product_id', 'quantity', 'price')


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product'] = ItemSerializer(instance.product).data
        return data



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
            'shipping_address',
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
