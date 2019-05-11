from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField(default='https://upload.wikimedia.org/wikipedia/common/7/72/Default-welcomer.png')
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.user}"
