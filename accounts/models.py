from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """
    My custom user  model
    
    first_name, last_name, password, username, is_user

    """
    REQUIRED_FIELDS = ['email']

    email = models.EmailField()
    phone_num = models.CharField(max_length=15, blank=True, null=True)
    job = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.username

