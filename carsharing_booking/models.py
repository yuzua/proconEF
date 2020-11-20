from django.db import models

# Create your models here.
class BookingModel(models.Model):
    
    user_id = models.IntegerField()
    car_id = models.IntegerField()
    start_day = models.DateField()
    start_time = models.CharField(max_length=16)
    end_day = models.DateField()
    end_time = models.CharField(max_length=16)