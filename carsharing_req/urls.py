from django.urls import path

from . import views
from .views import CarsharUser, CarsharUserSendMail

app_name = 'carsharing_req'
urlpatterns = [
    path('', views.index, name='index2'),
    path('index/', CarsharUser.as_view(), name='index'),
    path('sendmail/', CarsharUserSendMail.as_view(), name='sendmail')
]