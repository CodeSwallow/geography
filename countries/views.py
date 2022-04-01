from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import viewsets

from .models import Country
from .serializers import CountrySerializer

# Create your views here.


def main(request):
    countries = Country.objects.all()
    return render(request, 'countries/index.html', {"country_list": countries})


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(name__contains=name)
        return self.queryset

