from django.db import models
from django.contrib.auth.models import User


class Subscriptions(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="subscriptions")
    author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="subscribers")
    created_on = models.DateField(auto_now=True)
