from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Post model
    """    
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.CharField(max_length=255, blank=False)
    model = models.CharField(max_length=255, blank=False)
   

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.brand} {self.model} {self.production}'

