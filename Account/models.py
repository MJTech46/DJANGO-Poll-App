from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import custom_upload  # Import the custom upload path function

# Create your models here.
class CustomUser(AbstractUser):
    icon = models.ImageField(upload_to=custom_upload, null=True, blank=True)