from django.urls import path
from .views import ParkingHostCreate
from . import views

app_name = 'parking_req'
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/', views.test_ajax_response),
    path('create', ParkingHostCreate.as_view(), name='create'),
    path('edit', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('sample', views.sample, name='sample'),
]