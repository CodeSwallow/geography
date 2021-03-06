from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CountryViewSet, ContinentViewSet, CityViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'continents', ContinentViewSet, basename='continents')
router.register(r'cities', CityViewSet, basename='cities')

urlpatterns = [
    path('', include(router.urls))
]
