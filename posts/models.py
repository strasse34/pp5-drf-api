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
    production = models.IntegerField(blank=False, null=False, default='2024')
    other_details = models.CharField(max_length=260, default='other details')
    my_experience = models.TextField(blank=False, default='experience')
    image = models.ImageField(upload_to='pp5/images/cars', blank=False, null=False, default='default.jpg')
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.brand} {self.model} {self.production}'

  