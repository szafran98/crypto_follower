from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FollowedCrypto(models.Model):
    name = models.CharField(max_length=20)
    coin_id = models.CharField(max_length=20)
    who_follow = models.ForeignKey(User, on_delete=models.CASCADE)