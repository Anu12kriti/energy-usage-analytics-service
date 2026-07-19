from rest_framework import serializers
from .models import Site, EnergyReading


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"


class EnergyReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyReading
        fields = "__all__"