from django.urls import path

from . import views
from .views import CarsharUser

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', CarsharUser.as_view(), name='hello')
]