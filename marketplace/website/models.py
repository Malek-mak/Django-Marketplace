from django.db import models
from django.contrib.auth.models import User

class message(models.Model):
    message = models.TextField()
    sent_by = models.EmailField(blank=False, null=False)
    sent_to = models.TextField(null=True)
    about = models.CharField(null=True, max_length=200)
    
    def __str__(self):
        return f"{self.message}"