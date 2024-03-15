from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List of posts or create a post if logged in    
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),               
        ratings_average=Avg('ratings__stars'),               
    ).order_by('-created_at')

    
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    
    filterset_fields = [
        # user feed: filter the posts that the user is following the profiles' owner. 
        'owner__followed__owner__profile',
        # filter the posts that the user has liked.
        'likes__owner__profile',
        # filter the user's posts.
        'owner__profile',
    ]

    # posts are searchable by below fields:
    search_fields = [
        'owner__username',
        'brand',
        'model',
        'production',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
        'ratings_average',
    ]

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
        ratings_average=Avg('ratings__stars'),        
    ).order_by('-created_at')