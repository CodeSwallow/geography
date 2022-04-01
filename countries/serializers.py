from rest_framework import serializers

from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    capital_city = serializers.StringRelatedField(many=True, read_only=True)
    continents = serializers.StringRelatedField(many=True, read_only=True)
    is_transcontinental = serializers.ReadOnlyField()
    has_multiple_capital_cities = serializers.ReadOnlyField()

    class Meta:
        model = Country
        fields = "__all__"
