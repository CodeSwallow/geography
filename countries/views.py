from rest_framework import viewsets

from .models import Country, Continent, City
from .serializers import CountrySerializer, ContinentSerializer, CitySerializer

# Create your views here.


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset


class ContinentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset

