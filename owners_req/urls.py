from django.urls import path
from . import views
from django.conf.urls import url
from .views import CreateView, CreateCarView




app_name = 'owners_req'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', CreateView.as_view(), name='create'),
    path('createCar', CreateCarView.as_view(), name='createCar'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
]
