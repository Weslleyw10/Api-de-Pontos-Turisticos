from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import base
from rest_framework import routers

from rest_framework.authtoken.views import obtain_auth_token

from django.conf import settings
from django.conf.urls.static import static

from core.api.viewsets import TouristSpotsViewSet
from attractions.api.viewsets import AttractionsViewSet
from address.api.viewsets import AddressViewSet
from comments.api.viewsets import CommentsViewSet
from reviews.api.viewsets import ReviewViewSet

router = routers.DefaultRouter()
router.register(r'touristspots', TouristSpotsViewSet, basename='TouristSpots')
router.register(r'attractions', AttractionsViewSet)
router.register(r'address', AddressViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
