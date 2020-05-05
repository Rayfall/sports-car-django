from django.db import models

# Create your models here.
class CarsList(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.name)