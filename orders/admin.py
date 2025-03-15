from django.contrib import admin
from .models import OrderItems, Orders


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'customer_email',
        'customer_phone',
        'status'
    )
    search_fields = ('name', 'customer_name', 'customer_email', 'customer_phone')
    list_filter = ('status',)

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'price')
    list_filter = ('order', 'product')