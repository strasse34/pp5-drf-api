from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer, RatingCreateSerializer

class RatingList(generics.ListCreateAPIView):
    """
    List ratings or create a rating if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RatingCreateSerializer
        return RatingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a rating by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()