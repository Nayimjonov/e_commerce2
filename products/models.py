from django.db import models
from categories.models import Categories


class Products(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
