from django.contrib import admin
from .models import SecondHandCarAIModel, SecondHandCarInfoModel, SecondHandCarPriceModel

# Register your models here.
admin.site.register(SecondHandCarAIModel)
admin.site.register(SecondHandCarInfoModel)
admin.site.register(SecondHandCarPriceModel)