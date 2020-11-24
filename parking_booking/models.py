from django.db import models
from django.utils import timezone

# Create your models here.

class BookingInfoModel(models.Model):
     user_id = models.IntegerField(default=0, verbose_name='ユーザID')
     parking_id = models.IntegerField(max_length=32, verbose_name='駐車場ID')
     car_id = models.IntegerField(max_length=32, verbose_name='車ID')
     start_day = models.DateField(max_length=32, verbose_name='利用開始日')
     end_day = models.DateField(max_length=32, verbose_name='利用終了日')
     start_time = models.IntegerField(max_length=8, verbose_name='利用開始時間')
     end_time = models.IntegerField(max_length=8, verbose_name='利用終了時間')
     charge = models.IntegerField(max_length=8, verbose_name='利用料金')
     regist_date = models.DateTimeField(default=timezone.now, verbose_name='登録日時')

     def __str__(self):
        return '<booking_id=' + str(self.id) + '>'