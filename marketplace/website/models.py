from django.db import models
from Users.models import User # Assuming User is the custom user model defined in Users app

class message(models.Model):
    message = models.TextField()
    sent_by = models.EmailField(blank=False, null=False)
    sent_to = models.TextField(null=True)
    about = models.CharField(null=True, max_length=200)
    
    def __str__(self):
        return f"{self.message}"