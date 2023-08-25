from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model class"""
    author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='authored')
    category = models.ForeignKey(
        "Category", on_delete=models.DO_NOTHING, related_name='posts')
    title = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now=True)
    image_url = models.CharField(max_length=150)
    content = models.CharField(max_length=10000)
    approved = models.BooleanField(default=True)
    reactions = models.ManyToManyField("Reaction", through="PostReactions")
    tags = models.ManyToManyField("Tag", through="PostTags")
