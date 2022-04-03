from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'continents', ContinentViewSet, basename='continents')

urlpatterns = [
    path('', include(router.urls))
]

