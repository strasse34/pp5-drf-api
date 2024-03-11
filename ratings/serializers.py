from rest_framework import serializers
from django.db import IntegrityError
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for the rating model    
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Rating
        fields = ['id','owner', 'post', 'created_at','updated_at', 'stars']
        read_only_fields = ['owner', 'created_at']
        

    def create(self, validated_data):
        """
        Check if the user has already rated the post
        """
        user = self.context['request'].user
        post = validated_data['post']
        
        if Rating.objects.filter(owner=user, post=post).exists():
            raise serializers.ValidationError({'detail': 'You have already rated this post.'})

class RatingCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Rating
        fields = ['id','owner', 'post', 'created_at','updated_at', 'stars']

    def validate(self, data):
        """
        Validating
        """
        user = self.context['request'].user
        post_owner = data['post'].owner

        # Check if the user is the owner of the post
        if user == post_owner:
            raise serializers.ValidationError({'detail': 'You cannot rate your own post.'})

        # Check if the user has already rated the post
        if Rating.objects.filter(owner=user, post=data['post']).exists():
            raise serializers.ValidationError({'detail': 'You have already rated this post.'})

        return data