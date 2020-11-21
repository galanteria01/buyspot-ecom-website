from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    productTitle = models.CharField(max_length=30)
    slug = models.SlugField()
    price = models.BigIntegerField()
    about = models.TextField()
    thumbnail = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    seller = models.CharField(max_length=30)

    def __str__(self):
        return self.productTitle

    def snippet(self):
        return self.about[:30] + '...'