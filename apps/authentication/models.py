from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=500,null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/',null=True, blank=True)