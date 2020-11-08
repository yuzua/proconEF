from django.db import models

# Create your models here.
class BookingModel(models.Model):
    
    user_id = models.IntegerField()
    car_id = models.IntegerField()
    start_time = models.CharField(max_length=16)
    end_time = models.CharField(max_length=16)