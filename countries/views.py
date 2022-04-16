from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Country, Continent, City
from .serializers import CountrySerializer, ContinentSerializer, CitySerializer

import random


# Create your views here.


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    NUMBER_COUNTRIES = 5
    NUMBER_OPTIONS = 3

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset

    @action(detail=False)
    def generate_quiz(self, request):
        all_countries = Country.objects.all()
        if all_countries.count() == 0:
            return Response({'response': 'No data found'})
        all_continents = Continent.objects.all()
        countries = list(all_countries)
        random_countries = random.sample(countries, self.NUMBER_COUNTRIES)
        serializer = self.get_serializer(random_countries, many=True)
        for item in serializer.data:
            country_options = list(all_countries.exclude(pk=item['id']))
            random_countries = random.sample(country_options, self.NUMBER_OPTIONS)
            item['capital_options'] = [country.capital_city.first().name for country in random_countries]
            continent_options = list(all_continents.exclude(name__in=item['continents']))
            random_continents = random.sample(continent_options, self.NUMBER_OPTIONS)
            item['continent_options'] = [continent.name for continent in random_continents]
        return Response(serializer.data)


class ContinentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    NUMBER_CONTINENTS = 5
    NUMBER_OPTIONS = 3

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset

    @action(detail=False)
    def generate_quiz(self, request):
        if Continent.objects.count() == 0:
            return Response({'response': 'No data found'})
        continents = list(Continent.objects.exclude(name='Antarctica'))
        random_continents = random.sample(continents, self.NUMBER_CONTINENTS)
        serializer = self.get_serializer(random_continents, many=True)
        for item in serializer.data:
            countries = list(Country.objects.exclude(continents__continent=item['id']))
            random_countries = random.sample(countries, self.NUMBER_OPTIONS)
            item['country_options'] = [country.name for country in random_countries]
        return Response(serializer.data)


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    NUMBER_CITIES = 5
    NUMBER_OPTIONS = 3

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset

    @action(detail=False)
    def generate_quiz(self, request):
        if City.objects.count() == 0:
            return Response({'response': 'No data found'})
        cities = list(City.objects.all())
        random_cities = random.sample(cities, self.NUMBER_CITIES)
        serializer = self.get_serializer(random_cities, many=True)
        for item in serializer.data:
            countries = list(Country.objects.exclude(name=item['country']))
            random_countries = random.sample(countries, self.NUMBER_OPTIONS)
            item['country_options'] = [c.name for c in random_countries]
        return Response(serializer.data)
