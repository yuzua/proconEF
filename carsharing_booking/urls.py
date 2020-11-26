from django.urls import path

from . import views
from .views import ReservationList

app_name = 'carsharing_booking'
urlpatterns = [
    path("", views.test_ajax_app),
    path("map/", views.map, name='map'),
    path('booking/<int:num>', views.booking, name='booking'),
    path('checkbooking/', views.checkBooking, name='checkbooking'),
    path('push/', views.push, name='push'),
    path('list/', ReservationList.as_view(), name='list'),
]