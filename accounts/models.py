from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# creating 'ProfileUser' model
class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, default='', blank=True)
    last_name = models.CharField(max_length=40, default='', blank=True)
    description = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    profile_picture = models.URLField(default='https://upload.wikimedia.org/wikipedia/common/7/72/Default-welcomer.png')

    def __str__(self):
        return f"{self.user}"

# function that creates 'ProfileUser' automatically after sign up new 'User'
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ProfileUser.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)
