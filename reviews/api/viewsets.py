from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .serializers import ReviewSerializer
from reviews.models import Reviews

class ReviewViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer