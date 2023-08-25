from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authors_comments")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=100)