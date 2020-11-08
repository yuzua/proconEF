from django.urls import path

from . import views

app_name = 'carsharing_booking'
urlpatterns = [
    path("", views.test_ajax_app),
    path("ajax/", views.test_ajax_response),
]