from rest_framework import generics
from apps.cars.serializers import CarsListSerializer
from apps.cars.models import CarsList

class CreateView(generics.ListCreateAPIView):
    queryset = CarsList.objects.all()
    serializer_class = CarsListSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarsList.objects.all()
    serializer_class = CarsListSerializer