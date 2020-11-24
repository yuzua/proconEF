from django.urls import path

from . import views

app_name = 'carsharing_booking'
urlpatterns = [
    path("", views.test_ajax_app),
    path("ajax/", views.test_ajax_response),
    path("map/", views.map, name='map'),
    path('booking/<int:num>', views.booking, name='booking'),
    path('postbooking', views.postBooking, name='postbooking'),
]