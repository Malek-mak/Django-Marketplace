from django.db import models
from Users.models import User
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"
    
class item(models.Model):
    name = models.CharField(max_length=255)
    discription = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    categoty = models.ForeignKey(category, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images', null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"