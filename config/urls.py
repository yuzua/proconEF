"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('carsharing_req/', include('carsharing_req.urls')),
    path('carsharing_booking/', include('carsharing_booking.urls')),
    path('owners_req/', include('owners_req.urls')),
    path('parking_req/', include('parking_req.urls')),
    path('secondhandcar/', include('secondhandcar.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]