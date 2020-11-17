from django.urls import path
from . import views
from django.conf.urls import url
from .views import CreateView, CreateCarView, ParkingHostCreate




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
    path('createParking', ParkingHostCreate.as_view(), name='createParking'),
    path('editParking', views.editParking, name='editParking'),
    path('deleteCar/<int:num1>', views.deleteParking, name='deleteParking'),
    path('parkingplace', views.parkingplace, name='parkingplace'),
    path('carparkinglist', views.carparkinglist, name='carparkinglist'),
]
