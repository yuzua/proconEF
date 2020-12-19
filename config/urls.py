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
from django.contrib.staticfiles.urls import static

from . import settings

urlpatterns = [
    path('', include('administrator.urls')),
    path('carsharing_req/', include('carsharing_req.urls')),
    path('carsharing_booking/', include('carsharing_booking.urls')),
    path('owners_req/', include('owners_req.urls')),
    path('parking_req/', include('parking_req.urls')),
    path('secondhandcar/', include('secondhandcar.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('administrator/', include('administrator.urls')),
    path('parking_booking/', include('parking_booking.urls')),
    path('survey/', include('survey.urls')),
]
# メディア配信を可能にする設定【開発用】
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)