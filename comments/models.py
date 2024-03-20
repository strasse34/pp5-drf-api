from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

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
    ratings_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        # Calculate rating average whenever a new rating is added or modified
        if self.pk:  # Check if the comment is being updated
            old_stars = Comment.objects.get(pk=self.pk).stars
            self.ratings_count += 1 if self.stars > 0 and old_stars == 0 else 0
            self.ratings_count -= 1 if self.stars == 0 and old_stars > 0 else 0
        else:  # New comment
            self.ratings_count = 1 if self.stars > 0 else 0

        super().save(*args, **kwargs)
