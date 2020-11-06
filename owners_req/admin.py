from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(HostUserModel)
admin.site.register(Post)
admin.site.register(ParentCategory)
admin.site.register(Category)