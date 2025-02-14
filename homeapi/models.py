from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('user', 'User')], default='user')
    full_name = models.CharField(max_length=255, blank=True, null=True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
