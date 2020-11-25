from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    email = models.EmailField(max_length=50)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def update_profile_signal(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

