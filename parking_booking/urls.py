from django.urls import path
from . import views
from .views import ParkingBookingCreate

app_name = 'parking_booking'
urlpatterns = [
    path('', views.index, name='index'),
    path("ajax/", views.test_ajax_response),
    path("map/", views.map, name='map'),
    path('create', ParkingBookingCreate.as_view(), name='create'),
]