from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from decimal import Decimal


class Comment(models.Model):
    """
    Comment model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1000, blank=False, default='comment')
    stars = models.PositiveIntegerField(default=0)    
    ratings_average = models.FloatField(default=0)  

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        # Get the total number of comments for the post
        total_comments = self.post.comment_set.count()

        # Calculate total stars for all comments of the post
        total_stars = self.post.comment_set.aggregate(models.Sum('stars'))['stars__sum']

        # Calculate ratings_average
        if total_stars is not None and total_comments > 0:
            # Calculate average and round to 2 decimal places
            average = Decimal(total_stars) / Decimal(total_comments)
            self.ratings_average = round(average, 2)
        else:
            self.ratings_average = 0

        super().save(*args, **kwargs)
