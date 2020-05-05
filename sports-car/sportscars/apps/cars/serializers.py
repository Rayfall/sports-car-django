from rest_framework import serializers
from apps.cars.models import CarsList


class CarsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarsList
        fields = ('id', 'name')