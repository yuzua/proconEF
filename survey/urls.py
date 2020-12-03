from django.urls import path
from .views import Survey
from . import views

app_name = 'survey'
urlpatterns = [
    path('', views.index, name='index'),
    path('questionnaire', Survey.as_view(), name='questionnaire'),
]