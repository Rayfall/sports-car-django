from django.db import models

# Create your models here.
class CarsList(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.name

class ModelInformation(models.Model):
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=50)
    price = models.CharField(max_length=200)
    drivetrain = models.CharField(max_length=3)
    car = models.ForeignKey(CarsList, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"

    def __str__(self):
        return self.car + " " + self.make + " " + self.drivetrain + " " + self.year + " " + self.price