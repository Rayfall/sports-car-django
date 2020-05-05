from rest_framework import serializers
from apps.cars.models import CarsList, ModelInformation


class CarsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarsList
        fields = ('id', 'name',)

class ModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ModelInformation
        fields = ('id', 'car', 'year', 'price', 'make', 'drivetrain')