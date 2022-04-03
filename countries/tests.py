from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Country, City, Continent


# Create your tests here.


class GeographyViewSetsTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.country_1 = Country.objects.create(name='United States of America', population=331002651, land_area=9147420)
        cls.country_2 = Country.objects.create(name='South Africa', population=59308690, land_area=1213090)
        cls.country_3 = Country.objects.create(name='Russia', population=145934462, land_area=16376870)
        cls.country_4 = Country.objects.create(name='China', population=1439323776, land_area=9388211)
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
        cls.capital_6 = City.objects.create(name='Beijing', population=0, country=cls.country_4,
                                            is_country_capital=True)
        cls.continent_1 = Continent.objects.create(name='North America', population=592072212, land_area=21330000)
        cls.continent_2 = Continent.objects.create(name='Africa', population=1340598147, land_area=29648481)
        cls.continent_3 = Continent.objects.create(name='Europe', population=747636026, land_area=22134900)
        cls.continent_4 = Continent.objects.create(name='Asia', population=4641054775, land_area=31033131)
        cls.continent_1.countries.add(cls.country_1)
        cls.continent_2.countries.add(cls.country_2)
        cls.continent_3.countries.add(cls.country_3)
        cls.continent_4.countries.add(cls.country_3)
        cls.continent_4.countries.add(cls.country_4)

    def test_retrieve_country(self):
        """
        Ensure we can retrieve a country object.
        """
        dict_keys = ['name', 'population', 'land_area', 'is_transcontinental', 'has_multiple_capital_cities']
        url = reverse('countries-detail', args=['1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'United States of America')
        for key in dict_keys:
            self.assertIn(key, response.data)

    def test_can_retrieve_all_countries(self):
        """
        Ensure we can retrieve a list of all countries.
        """
        url = reverse('countries-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

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

    def test_retrieve_city(self):
        """
        Ensure we can retrieve a city object.
        """
        dict_keys = ['name', 'population', 'is_country_capital', 'special_note', 'country']
        url = reverse('cities-detail', args=['2'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Pretoria')
        for key in dict_keys:
            self.assertIn(key, response.data)

    def test_can_retrieve_all_cities(self):
        """
        Ensure we can retrieve a list of all cities.
        """
        url = reverse('cities-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_country_of_capital_city(self):
        """
        Ensure we can view the country of the capital city
        """
        url = reverse('cities-detail', args=['2'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['country'], 'South Africa')

    def test_city_special_note(self):
        """
        Ensure we can view the country of the capital city
        """
        self.assertEqual(str(self.capital_1), 'Washington, D.C.')
        self.assertEqual(str(self.capital_2), 'Pretoria (Administrative)')

    def test_retrieve_continent(self):
        """
        Ensure we can retrieve a continent object.
        """
        dict_keys = ['name', 'population', 'land_area', 'countries', 'country_count']
        url = reverse('continents-detail', args=['2'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Africa')
        for key in dict_keys:
            self.assertIn(key, response.data)

    def test_can_retrieve_all_continents(self):
        """
        Ensure we can retrieve a list of all continents.
        """
        url = reverse('continents-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_continent_country_count(self):
        """
        Ensure we can view number of countries in a continent
        """
        url_1 = reverse('continents-detail', args=['2'])
        response_1 = self.client.get(url_1)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_1.data['name'], 'Africa')
        self.assertEqual(response_1.data['country_count'], 1)
        url_2 = reverse('continents-detail', args=['4'])
        response_2 = self.client.get(url_2)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.data['name'], 'Asia')
        self.assertEqual(response_2.data['country_count'], 2)
