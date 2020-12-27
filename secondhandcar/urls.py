from django.urls import path

from . import views

app_name = 'secondhandcar'
urlpatterns = [
    path('', views.index, name='index'),
    path('import_csv', views.importCSV, name='import_csv'),
]