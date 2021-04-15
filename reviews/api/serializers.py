from rest_framework.serializers import ModelSerializer
from reviews.models import Reviews

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
