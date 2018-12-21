"""Temperature_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from api_app import views, viewsets

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'TempModel', viewsets.TempViewSet)
router.register(r'WaterModel', viewsets.WaterViewSet)
router.register(r'DetectionModel', viewsets.DetectionViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('upload/temp/', views.post, name='temp'),
    path('upload/water/', views.post_water, name='level'),
    path('upload/waterdetected/', views.post_water_detected, name='detected'),
    path(r'api/', include(router.urls))
]
