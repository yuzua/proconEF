from django.contrib import admin
from .models import ParkingUserModel, ParkingUsageModel


# Register your models here.
admin.site.register(ParkingUserModel)
admin.site.register(ParkingUsageModel)