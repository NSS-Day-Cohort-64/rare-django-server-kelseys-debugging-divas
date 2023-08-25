from django.db import models
from django.contrib.auth.models import User

class PostReaction(models.Model):
    reaction = models.ForeignKey("Reaction", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)