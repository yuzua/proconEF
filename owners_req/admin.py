from django.contrib import admin
from .models import *


# class CarList(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super(CarList, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(author=request.user)



admin.site.register(HostUserModel)
admin.site.register(CarInfoModel)
admin.site.register(ParentCategory)
admin.site.register(Category)