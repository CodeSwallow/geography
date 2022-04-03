from rest_framework import serializers

from .models import Country, Continent, City


class CountrySerializer(serializers.ModelSerializer):
    capital_city = serializers.StringRelatedField(many=True, read_only=True)
    continents = serializers.StringRelatedField(many=True, read_only=True)
    is_transcontinental = serializers.ReadOnlyField()
    has_multiple_capital_cities = serializers.ReadOnlyField()

    class Meta:
        model = Country
        fields = "__all__"


class ContinentSerializer(serializers.ModelSerializer):
    countries = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Continent
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = City
        fields = "__all__"
