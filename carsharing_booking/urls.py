from django.urls import path

from . import views
from .views import ReservationList

app_name = 'carsharing_booking'
urlpatterns = [
    path("", views.select, name='select'),
    # path("", views.test_ajax_app),
    path("map/", views.map, name='map'),
    path('car/', views.car, name='car'),
    # path('car/<int:num>', views.booking_car, name='booking_car'),
    path('booking/<int:num>', views.booking, name='booking'),
    path('checkbooking/', views.checkBooking, name='checkbooking'),
    path('push/', views.push, name='push'),
    path('list/', ReservationList.as_view(), name='list'),
]