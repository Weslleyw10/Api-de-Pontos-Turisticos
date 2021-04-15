from rest_framework.serializers import ModelSerializer
from core.models import TouristSpots
from attractions.api.serializers import AttractionsSerializer
from comments.api.serializers import CommentsSerializer
from address.api.serializers import AddressSerializer
from rest_framework.fields import SerializerMethodField


class TouristSpotsSerializer(ModelSerializer):
    attractions = AttractionsSerializer(many=True)
    comment = CommentsSerializer(many=True)
    address = AddressSerializer()
    fullDescription = SerializerMethodField()

    class Meta:
        model = TouristSpots
        fields = ('id', 'name', 'description', 'approved', 'image', 'address', 'attractions', 'comment', 'fullDescription')

    def get_fullDescription(self, obj):
        return '%s - %s' % (obj.name, obj.description)