from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model    
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'created_at', 'followed', 'followed_name'
        ]

    def validate(self, data):
        """
        Check if the owner and followed users are different.
        """
        owner = self.context['request'].user
        followed = data['followed']

        if owner == followed:
            raise serializers.ValidationError({'detail': "You can't follow yourself."})

        return data

    def create(self, validated_data):
        """
        Preventing duplicate following.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'You have already followed this user!'})
