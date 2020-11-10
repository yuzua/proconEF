from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ParkingUserModel(models.Model):

    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    #carsharing_id = models.IntegerField(max_length=8)
    #parking_id = models.CharField(max_length=32)
    lat = models.CharField(max_length=64)
    lng = models.CharField(max_length=64)
    day = models.DateField()
    parking_type = models.CharField(max_length=32)
    width = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    length = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    height = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    def __str__(self):
        return '<parking_id=' + str(self.id) + '>'  
