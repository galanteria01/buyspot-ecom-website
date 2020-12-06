from items.models import Item
from accounts.models import Profile
from django.db import models

# Create your models here.
class orderItem(models.Model):
    product = models.OneToOneField(Item,on_delete=models.SET_NULL,null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.productTitle

class Order(models.Model):
    ref_code = models.CharField(max_length=30)
    owner = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(orderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    # payment_details = models.ForeignKey(Payment,null=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner,self.ref_code)