from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ParkingUserModel(models.Model):

    #carsharing_id = models.IntegerField(max_length=8)
    #parking_id = models.CharField(max_length=32)
    coordinate = models.CharField(max_length=64)
    day = models.DateField()
    parking_type = models.CharField(max_length=32)
    width = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    length = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    height = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    car_id = models.IntegerField(default=0)
    def __str__(self):
        return '<carsharing_id=' + str(self.id) + '>'  
