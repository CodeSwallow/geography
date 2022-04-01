from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Country, City, Continent


# Create your tests here.


class CountryModelTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.country_1 = Country.objects.create(name='United States of America', population=331002651, land_area=9147420)
        cls.country_2 = Country.objects.create(name='South Africa', population=59308690, land_area=1213090)
        cls.country_3 = Country.objects.create(name='Russia', population=145934462, land_area=16376870)
        cls.capital_1 = City.objects.create(name='Washington, D.C.', population=0, country=cls.country_1,
                                            is_country_capital=True)
        cls.capital_2 = City.objects.create(name='Pretoria', population=0, country=cls.country_2,
                                            is_country_capital=True, special_note='Administrative')
        cls.capital_3 = City.objects.create(name='Cape Town', population=0, country=cls.country_2,
                                            is_country_capital=True, special_note='Legislative')
        cls.capital_4 = City.objects.create(name='Bloemfontein', population=0, country=cls.country_2,
                                            is_country_capital=True, special_note='Judicial')
        cls.capital_5 = City.objects.create(name='Moscow', population=0, country=cls.country_3,
                                            is_country_capital=True)
        cls.continent_1 = Continent.objects.create(name='North America', population=592072212, land_area=21330000)
        cls.continent_2 = Continent.objects.create(name='Africa', population=1340598147, land_area=29648481)
        cls.continent_3 = Continent.objects.create(name='Europe', population=747636026, land_area=22134900)
        cls.continent_4 = Continent.objects.create(name='Asia', population=4641054775, land_area=31033131)
        cls.continent_1.countries.add(cls.country_1)
        cls.continent_2.countries.add(cls.country_2)
        cls.continent_3.countries.add(cls.country_3)
        cls.continent_4.countries.add(cls.country_3)

    def test_retrieve_country(self):
        """
        Ensure we can retrieve a country object.
        """
        url = reverse('countries-detail', args=['1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'United States of America')

    def test_country_has_one_capital(self):
        """
        Ensure country with one capital displays attribute correctly.
        """
        url = reverse('countries-detail', args=['3'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['has_multiple_capital_cities'], False)
        self.assertEqual(len(response.data['capital_city']), 1)

    def test_country_has_multiple_capitals(self):
        """
        Ensure country with multiple capitals displays attribute correctly.
        """
        url = reverse('countries-detail', args=['2'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['has_multiple_capital_cities'], True)
        self.assertEqual(len(response.data['capital_city']), 3)

    def test_country_in_one_continent(self):
        """
        Ensure country is not transcontinental.
        """
        url = reverse('countries-detail', args=['1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_transcontinental'], False)
        self.assertEqual(len(response.data['continents']), 1)

    def test_country_is_transcontinental(self):
        """
        Ensure country is transcontinental.
        """
        url = reverse('countries-detail', args=['3'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_transcontinental'], True)
        self.assertEqual(len(response.data['continents']), 2)
