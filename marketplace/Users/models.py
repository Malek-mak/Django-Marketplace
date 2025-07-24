from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser): 

    username = models.CharField(max_length=150, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    joined_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=[('buyer', 'Buyer'), ('seller', 'Seller')], blank=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'auth_user'
        ordering = ['-joined_at']
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        
        