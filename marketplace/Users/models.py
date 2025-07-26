from django.db import models
from django.contrib.auth.models import AbstractUser
from items.models import item



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
        
        
class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(item, on_delete=models.CASCADE, related_name='cart_items')
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f"{self.user.username}'s cart"
    
class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(item, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)  # Assuming a positive integer for
    order_date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending')
    
        
        