from django.urls import path
from . import views
from django.conf.urls import url
from .views import CreateView




app_name = 'owners_req'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', CreateView.as_view(), name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
]
