from django.db import models
from django.utils import timezone

# Create your models here.
class BookingModel(models.Model):
    
    user_id = models.IntegerField()
    car_id = models.IntegerField()
    start_day = models.CharField(verbose_name='予約開始日', max_length=10)
    start_time = models.CharField(verbose_name='予約開始時刻', max_length=5)
    end_day = models.CharField(verbose_name='予約終了日', max_length=10)
    end_time = models.CharField(verbose_name='予約終了時刻', max_length=5)
    charge = models.IntegerField(default=1000, verbose_name='利用料金')
    regist_date = models.DateTimeField(default=timezone.now, verbose_name='登録日時')

    def __str__(self):
        return '<carshar_booking_id=' + str(self.id) + '>'