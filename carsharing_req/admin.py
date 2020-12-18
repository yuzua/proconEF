from django.contrib import admin
from .models import CarsharUserModel, UsageModel


# Register your models here.
admin.site.register(CarsharUserModel)
admin.site.register(UsageModel)