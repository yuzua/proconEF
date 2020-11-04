from django.contrib import admin
from .models import HostUserModel, CarInfoModel


# Register your models here.
admin.site.register(HostUserModel)
admin.site.register(CarInfoModel)