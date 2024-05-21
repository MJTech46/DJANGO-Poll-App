from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    icon = models.ImageField(upload_to='UserIcons/', null=True, blank=True)