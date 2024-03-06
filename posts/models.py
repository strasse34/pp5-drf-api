from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model
    """    
  
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    car_company = models.CharField(max_length=255, blank=False, null=False)
    car_model = models.CharField(max_length=255, blank=False, null=False)
    car_product_year = models.IntegerField(blank=False, null=False)
    other_details = models.CharField(max_length=255, blank=False, null=False)
    my_experience = models.TextField(blank=True)
    car_image = models.ImageField(upload_to='pp5/images/cars', blank=False )
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
