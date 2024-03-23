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
        request = self.context.get('request')
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def validate(self, data):
        request = self.context.get('request')
        if not request:
            raise serializers.ValidationError("Request object not found in context.")

        user = request.user
        post = data.get('post')
        content = data.get('content')
        stars = data.get('stars')

        if post.owner == user:
            raise serializers.ValidationError("You cannot comment/rate on your own post.")

        existing_comment = Comment.objects.filter(owner=user, post=post)
        if existing_comment.exists():
            raise serializers.ValidationError("Multiple comments/ratings are not allowed. You can edit your last comment/rating.")

        if not content:
            raise serializers.ValidationError("Content is required for comment.")

        if stars is None:
            raise serializers.ValidationError("Stars are required for rating.")

        return data

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
