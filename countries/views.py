from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Country
from .serializers import CountrySerializer

# Create your views here.


def main(request):
    countries = Country.objects.all()
    return render(request, 'countries/index.html', {"country_list": countries})


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
