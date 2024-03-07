from rest_framework import serializers
from django.db import IntegrityError
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['owner', 'post', 'created_at', 'stars']
        read_only_fields = ['owner', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        post = validated_data['post']

        # Check if the user has already rated the post
        if Rating.objects.filter(owner=user, post=post).exists():
            raise serializers.ValidationError({'detail': 'You have already rated this post.'})

class RatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['post', 'stars']

    def create(self, validated_data):
        user = self.context['request'].user
        post = validated_data['post']

        # Check if the user has already rated the post
        if Rating.objects.filter(owner=user, post=post).exists():
            raise serializers.ValidationError({'detail': 'You have already rated this post.'})

        return super().create({**validated_data, 'owner': user})