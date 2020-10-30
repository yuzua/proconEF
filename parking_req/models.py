from django.db import models

# Create your models here.

class ParkingUserModel(models.Model):

    #carsharing_id = models.IntegerField(max_length=8)
    #parking_id = models.CharField(max_length=32)
    coordinate = models.CharField(max_length=64)
    day = models.DateField(max_length=10)
    parking_type = models.CharField(max_length=32)
    width = models.IntegerField(max_length=8)
    length = models.IntegerField(max_length=8)
    height = models.IntegerField(max_length=8)
    car_id = models.IntegerField(max_length=32)

    def __str__(self):
        return '<carsharing_id=' + str(self.id) + '>'  
