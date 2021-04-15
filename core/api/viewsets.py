from core.models import TouristSpots
from .serializers import TouristSpotsSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class TouristSpotsViewSet(ModelViewSet):
    serializer_class = TouristSpotsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset = TouristSpots.objects.all()

        if id:
            queryset = TouristSpots.objects.filter(id=id)
        if name:
            queryset = TouristSpots.objects.filter(name__icontains=name)
        if description:
            queryset = TouristSpots.objects.filter(description__icontains=description)

        return queryset
    
    # def list(self, request, *args, **kwargs):
    #     return Response({'teste':123})

    # def create(self, request, *args, **kwargs):
    #     return Response({'teste':request.data})

    # @action(methods=['POST', 'GET'], detail=True)
    # def denuncia(self, request, pk=None):
    #     pass

    # @action(methods=['POST', 'GET'], detail=False)
    # def denuncia2(self, request):
    #     pass


