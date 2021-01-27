from django.db import models
from django.core.validators import FileExtensionValidator
from parking_req .models import ParkingUserModel

# Create your models here.

class MediaModel(models.Model):
    attach = models.FileField(
            # upload_to='uploads/%Y/%m/%d/',
            upload_to='xlsx/',
            validators=[FileExtensionValidator(['xlsx', ])],
        )
    def __str__(self):
        return self.attach.url


class StationModel(models.Model):
    address = models.CharField(verbose_name='住所', max_length=255)
    lat = models.CharField(default=0, verbose_name='緯度', max_length=32)
    lng = models.CharField(default=0, verbose_name='経度', max_length=32)
    
    def __str__(self):
        return '<station_id=' + str(self.id) + '>'


class StationParkingModel(models.Model):
    parking_id =  models.ForeignKey(ParkingUserModel, on_delete=models.CASCADE, verbose_name='駐車場ID')
    station_id = models.ForeignKey(StationModel, on_delete=models.CASCADE, verbose_name='ステーションID')

    def __str__(self):
        return str(self.parking_id) + str(self.station_id)