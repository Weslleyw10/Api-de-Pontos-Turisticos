from rest_framework.serializers import ModelSerializer
from comments.models import Comments

class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
