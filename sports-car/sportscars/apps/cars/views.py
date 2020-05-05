from rest_framework import generics
from apps.cars.serializers import CarsListSerializer, ModelSerializer
from apps.cars.models import CarsList, ModelInformation

class CreateView(generics.ListCreateAPIView):
    queryset = CarsList.objects.all()
    serializer_class = CarsListSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarsList.objects.all()
    serializer_class = CarsListSerializer

class CreateModelInformation(generics.ListCreateAPIView):
    queryset = ModelInformation.objects.all()
    serializer_class = ModelSerializer

    def perform_create(self, serializer):
        serializer.save()

class ModelDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModelInformation.objects.all()
    serializer_class = ModelSerializer