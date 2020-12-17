from django.urls import path
from . import views
from django.conf.urls import url
from .views import CreateView, CreateCarView, SettingInfo, CreateDateView




app_name = 'owners_req'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', CreateView.as_view(), name='create'),
    path('createCar', CreateCarView.as_view(), name='createCar'),
    path('edit', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('editCar', views.editCar, name='editCar'),
    path('deleteCar/<int:num1>', views.deleteCar, name='deleteCar'),
    path('carlist', views.carlist, name='carlist'),
    path('ownerslist', views.ownerslist, name='ownerslist'),
    #path('carparkinglist', views.carparkinglist, name='carparkinglist'),
    path('settinginfo', SettingInfo.as_view(), name='settinginfo'),
    path('createDate', CreateDateView.as_view(), name='createDate'),
    path('check', views.check, name='check'),
]
