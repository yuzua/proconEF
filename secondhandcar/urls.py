from django.urls import path

from . import views

app_name = 'secondhandcar'
urlpatterns = [
    path('', views.index, name='index'),
    path('import_csv', views.importCSV, name='import_csv'),
    path('export_csv', views.exportCSV, name='export_csv'),
    path('recommend_car', views.recommend_car, name='recommend_car'),
]