from django.urls import path

from . import views
from .views import ReservationList, DeleteBooking

app_name = 'carsharing_booking'
urlpatterns = [
    path("", views.select, name='select'),
    # path("", views.test_ajax_app),
    path("map/", views.map, name='map'),
    path("geo/", views.geo, name='geo'),
    path('car/', views.car, name='car'),
    path('history/', views.history, name='history'),
    path('car/<int:num>', views.booking_car, name='booking_car'),
    path('booking/<int:num>', views.booking, name='booking'),
    path('history/<int:num>', views.booking_history, name='booking_history'),
    path('checkbooking/', views.checkBooking, name='checkbooking'),
    path('push/', views.push, name='push'),
    path('reservation/', views.reservation, name='reservation'),
    path('list/', ReservationList.as_view(), name='list'),
    path('delete/', DeleteBooking.as_view(), name='delete'),
    path('delete/<str:flag>/<int:num>', DeleteBooking.as_view(), name='delete'),
]