from address.models import Address
from rest_framework.serializers import ModelSerializer
from address.models import Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


