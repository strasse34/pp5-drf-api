from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from django.db.models import Avg

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
        """
        Checking if the authenticated user is the owner of a post.
        """
        request = self.context.get('request')
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Checking if the authenticated user has liked a post and, if so, providing the id of that like.
        """
        user = self.context.get('request').user
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
        comments = obj.comment_set.all()  # Assuming 'comment_set' is the related name for comments
        if comments.exists():
            return comments.aggregate(Avg('stars'))['stars__avg']
        return None

    def get_ratings_count(self, obj):
        """
        Get the count of ratings for the post.
        """
        comments = obj.comment_set.all()  # Assuming 'comment_set' is the related name for comments
        return comments.count()

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
