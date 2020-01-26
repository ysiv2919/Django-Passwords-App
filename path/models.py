from django.db import models
from django.contrib.auth.models import User

class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.CharField(max_length=50)
    password = models.CharField(max_length=200)