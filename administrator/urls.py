from django.urls import path
from . import views
from .views import ParkingAdminCreate, CreateCarAdminView, SettingAdminInfo, UploadData

app_name = 'administrator'
urlpatterns = [
    path('', views.check_superuser, name='check_superuser'),
    path('index/', views.index, name='index'),
    path('ajax/', views.test_ajax_response),
    path('create/', ParkingAdminCreate.as_view(), name='create'),
    path('admin_main/', views.admin_main, name='admin_main'),
    path('edit/', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('createCar', CreateCarAdminView.as_view(), name='createCar'),
    path('settinginfo', SettingAdminInfo.as_view(), name='settinginfo'),
    path('upload_data', UploadData.as_view(), name='upload_data'),
]