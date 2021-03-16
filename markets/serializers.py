from rest_framework import serializers
from .models import Market

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class MarketUpdatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        exclude = ['registration_code']

