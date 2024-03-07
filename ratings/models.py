from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Rating(models.Model):
    """
    Rating model, related to 'owner' and 'post'.
    """
    STAR_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='ratings', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    stars = models.PositiveIntegerField(choices=STAR_CHOICES)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'