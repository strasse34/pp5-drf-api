from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CommentList(generics.ListCreateAPIView):
    """
    List of comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    # Filters the comments by post.
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        """
        Return the appropriate serializer class based on the request method.
        """
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return CommentSerializer
        return CommentDetailSerializer
