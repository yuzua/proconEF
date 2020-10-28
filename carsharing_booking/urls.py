from django.urls import path

from . import views

app_name = 'carsharing_booking'
urlpatterns = [
    path('', views.index, name='index'),
]