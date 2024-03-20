from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from django.db.models import Avg, Count
from comments.models import Comment  # Assuming the Comment model is imported from comments.models

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the post model    
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    ratings_average = serializers.SerializerMethodField() 
    ratings_count = serializers.SerializerMethodField()  

    def validate_image(self, value):
        """
        Validating images    
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_ratings_average(self, obj):
        """
        Calculate the average rating for the post.
        """
        return Comment.objects.filter(post=obj).aggregate(Avg('stars'))['stars__avg']

    def get_ratings_count(self, obj):
        """
        Get the count of ratings for the post.
        """
        return Comment.objects.filter(post=obj).count()

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'brand', 'model', 'production', 
            'other_details', 'my_experience', 'image',
            'like_id', 'likes_count','comments_count', 'ratings_count',  
            'ratings_average'  
        ]
