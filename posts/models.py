from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Post model
    """    
    
    CAR_BRAND_CHOICES = [
        ('toyota', 'Toyota'),
        ('volkswagen', 'Volkswagen'),
        ('audi', 'Audi'),
        ('ford', 'Ford'),
        ('honda', 'Honda'),
        ('bmw', 'BMW'),
        ('mercedes-Benz', 'Mercedes-Benz'),
        ('tesla', 'Tesla'),
        ('chevrolet', 'Chevrolet'),
        ('nissan', 'Nissan'),
        ('hyundai', 'Hyundai'),
        ('volvo', 'Volvo'),
        ('mazda', 'Mazda'),
        ('subaru', 'Subaru'),
        ('kia', 'Kia'),        
        ('renult', 'Renult'),
        ('porsche', 'Porsche'),
        
    ]

    PRODUCTION_CHOICES = [(str(year), str(year)) for year in range(2024, 1969, -1)]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.CharField(max_length=255, choices=CAR_BRAND_CHOICES, default='Toyota', blank=False)
    model = models.CharField(max_length=255, blank=False)
    production = models.IntegerField(choices=PRODUCTION_CHOICES, default=2024, blank=False, null=False)
    other_details = models.CharField(max_length=255)
    my_experience = models.TextField(blank=False)
    car_image = models.ImageField(upload_to='pp5/images/cars', blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.brand} {self.model} {self.production}'

