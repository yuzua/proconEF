from django.db import models
from django.utils import timezone
from parking_booking .models import ParkingBookingModel
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ParkingUserModel(models.Model):

    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    address = models.CharField(verbose_name='住所', max_length=255)
    lat = models.CharField(default=0, verbose_name='緯度', max_length=32)
    lng = models.CharField(default=0, verbose_name='経度', max_length=32)
    day = models.DateField(verbose_name='登録日')
    parking_type = models.CharField(max_length=5, verbose_name='駐車場タイプ')
    ground_type = models.CharField(max_length=32, verbose_name='土地タイプ')
    width = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    length = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    height = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    count = models.IntegerField(default=1, verbose_name='収容台数')
    admin = models.BooleanField(verbose_name='管理者', default=False)
    countflag = models.BooleanField(verbose_name='制限台数フラグ', default=True)
    def __str__(self):
        return '<parking_id=' + str(self.id) + '>'  


class ParkingUsageModel(models.Model):
    
    user_id = models.IntegerField()
    parking_id = models.IntegerField()
    booking_id = models.ForeignKey(ParkingBookingModel, verbose_name='予約番号', default=0, on_delete=models.PROTECT)
    start_day = models.CharField(verbose_name='開始日', max_length=10)
    start_time = models.CharField(verbose_name='開始時刻', max_length=5)
    end_day = models.CharField(verbose_name='終了日', max_length=10)
    end_time = models.CharField(verbose_name='終了時刻', max_length=5)
    charge = models.IntegerField(default=1000, verbose_name='利用料金')
    regist_date = models.DateTimeField(default=timezone.now, verbose_name='登録日時')

    def __str__(self):
        return '<parking_usage_id=' + str(self.id) + '>'