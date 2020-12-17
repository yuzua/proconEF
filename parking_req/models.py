from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ParkingUserModel(models.Model):

    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    address = models.CharField(verbose_name='住所', max_length=255)
    lat = models.CharField(default=0, verbose_name='緯度', max_length=32)
    lng = models.CharField(default=0, verbose_name='経度', max_length=32)
    day = models.DateField()
    parking_type = models.CharField(max_length=32)
    width = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    length = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    height = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    count = models.IntegerField(default=1, verbose_name='収容台数')
    admin = models.BooleanField(verbose_name='管理者', default=False)
    countflag = models.BooleanField(verbose_name='制限台数フラグ', default=True)
    def __str__(self):
        return '<parking_id=' + str(self.id) + '>'  
