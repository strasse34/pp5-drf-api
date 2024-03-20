from django.contrib.humanize.templatetags.humanize import naturaltime

from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model    
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def validate(self, value):
        """
        Custom validation to ensure the user cannot comment/rate their own post,
        cannot comment/rate multiple times on a single post, and must both comment and rate.
        """
        user = self.context['request'].user
        post = value['post']

        # Check if the user is the owner of the post
        if post.owner == user:
            raise serializers.ValidationError("You cannot comment/rate on your own post.")

        # Check if both content and stars are provided
        if 'content' not in value or 'stars' not in value:
            raise serializers.ValidationError("You must provide both content and stars.")

        # If it's an update, allow the operation
        if self.instance:
            return value

        # Check if the user has already commented/rated on the post
        existing_comment = Comment.objects.filter(owner=user, post=post).first()
        if existing_comment:
            raise serializers.ValidationError("You have already commented/rated on this post.")

        return value

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content', 'stars', 
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view    
    """
    post = serializers.ReadOnlyField(source='post.id')
