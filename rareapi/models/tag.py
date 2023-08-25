from django.db import models


class Tag(models.Model):
    """Tag model class"""
    label = models.CharField(max_length=25)
