from django.urls import path

from . import views
from .views import *

app_name = 'carsharing_req'
urlpatterns = [
    path('', views.index, name='first'),
    path('index/', CarsharUserInfo.as_view(), name='index'),
    path('carsharuserdata/', views.carsharuserdata, name='carsharuserdata'),
    path('pages/<int:num>', views.pages, name='pages'),
    path('create', CreateView.as_view(), name='create'),
    path('set_session/', views.set_session, name='set_session'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
]