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
    ratings_average = serializers.ReadOnlyField()

    def validate_car_image(self, value):
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
        chcking if the authenticated user is the owner of a post.
        """
        request = self.context.get('request')
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        checking if the authenticated user has liked a post and, if so, providing the id of that like.
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
        to round rating average
        """
        avg_rating = obj.ratings.aggregate(Avg('stars'))['stars__avg']
        return round(avg_rating, 1) if avg_rating is not None else None
    
    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'brand', 'model', 'production', 
            'other_details', 'my_experience', 'car_image',
            'like_id', 'comments_count', 'likes_count', 'ratings_average'
        ]

    def to_representation(self, instance):
        """
        Customizing 'ratings_average' Field Representation
        """
        representation = super().to_representation(instance)
        avg_rating = self.get_ratings_average(instance)
        representation['ratings_average'] = f"{avg_rating:.1f}" if avg_rating is not None else None
        return representation
