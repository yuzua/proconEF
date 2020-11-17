from django.urls import path
from . import views
from .views import ParkingAdminCreate

app_name = 'administrator'
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/', views.test_ajax_response),
    path('create', ParkingAdminCreate.as_view(), name='create'),
]