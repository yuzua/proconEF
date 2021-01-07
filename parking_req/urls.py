from django.urls import path
from .views import ParkingHostCreate, ParkingLoaningCreate
from . import views

app_name = 'parking_req'
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/', views.test_ajax_response),
    path('create', ParkingHostCreate.as_view(), name='create'),
    path('checkparking', views.checkparking, name='checkparking'),
    path('edit', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('sample', views.sample, name='sample'),
    path('loaning/', ParkingLoaningCreate.as_view(), name='loaning'),
    path('push/', views.push, name='push'),
]