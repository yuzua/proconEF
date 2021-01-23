from django.contrib import admin
from .models import CarsharUserModel, UsageModel, UserFavoriteCarModel


# Register your models here.
admin.site.register(CarsharUserModel)
admin.site.register(UsageModel)
admin.site.register(UserFavoriteCarModel)