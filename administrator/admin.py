from django.contrib import admin
from .models import MediaModel, StationModel, StationParkingModel

# Register your models here.
admin.site.register(MediaModel)
admin.site.register(StationModel)
admin.site.register(StationParkingModel)