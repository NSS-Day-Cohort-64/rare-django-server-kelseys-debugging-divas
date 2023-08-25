from django.db import models


class Category(models.Model):
    """Category model class"""
    label = models.CharField(max_length=25)
