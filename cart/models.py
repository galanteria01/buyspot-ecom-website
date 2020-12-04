from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True,auto_now_add=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)



    def __unicode__(self):
        return "%s"