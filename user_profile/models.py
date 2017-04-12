from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=1000, default="")
    emoji = models.CharField(max_length=10, default="")


    def __str__(self):
        return str(self.emoji)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
