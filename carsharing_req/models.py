from django.db import models
from carsharing_booking .models import BookingModel
from django.utils import timezone

# Create your models here.

class CarsharUserModel(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    zip01 = models.IntegerField()
    pref01 = models.CharField(max_length=100)
    addr01 = models.CharField(max_length=100)
    addr02 = models.CharField(max_length=100)
    system_flag = models.IntegerField(default=0)

    
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'


class UsageModel(models.Model):
    
    user_id = models.IntegerField()
    car_id = models.IntegerField()
    booking_id = models.ForeignKey(BookingModel, verbose_name='予約番号', default=0, on_delete=models.PROTECT)
    start_day = models.CharField(verbose_name='開始日', max_length=10)
    start_time = models.CharField(verbose_name='開始時刻', max_length=5)
    end_day = models.CharField(verbose_name='終了日', max_length=10)
    end_time = models.CharField(verbose_name='終了時刻', max_length=5)
    charge = models.IntegerField(default=1000, verbose_name='利用料金')
    regist_date = models.DateTimeField(default=timezone.now, verbose_name='登録日時')

    def __str__(self):
        return '<carshar_usage_id=' + str(self.id) + '>'