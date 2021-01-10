from django.urls import path

from . import views

app_name = 'secondhandcar'
urlpatterns = [
    path('', views.price, name='price'),
    path('import_csv', views.importCSV, name='import_csv'),
    path('export_csv', views.exportCSV, name='export_csv'),
    path('recommend_car', views.recommend_car, name='recommend_car'),
    path('search/', views.search, name='search'),
    path('search/<int:num>', views.search, name='search'),
    path('detail/<int:num>', views.detail, name='detail'),
    path('test', views.test, name='test'),
]