from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"
