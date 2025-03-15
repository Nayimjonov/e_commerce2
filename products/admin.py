from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)