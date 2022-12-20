from django.db import models
from django.contrib.auth.models import User


class  places(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='Pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)







