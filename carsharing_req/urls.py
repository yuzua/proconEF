from django.urls import path

from . import views
from .views import CarsharUser

app_name = 'carsharing_req'
urlpatterns = [
    path('', views.index, name='index2'),
    path('index/', CarsharUser.as_view(), name='index')
]