from django.urls import path

from . import views
from .views import CarsharUser, CarsharUserSendMail, CreateView

app_name = 'carsharing_req'
urlpatterns = [
    path('', views.index, name='first'),
    path('index/', CarsharUser.as_view(), name='index'),
    path('create', CreateView.as_view(), name='create'),
    path('set_session/', views.set_session, name='set_session'),
]