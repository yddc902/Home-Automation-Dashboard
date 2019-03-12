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
from api_app import views, viewsets, endpoints

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'TempModel', viewsets.TempViewSet)
router.register(r'WaterModel', viewsets.WaterViewSet)
router.register(r'DetectionModel', viewsets.DetectionViewSet)
router.register(r'MailModel', viewsets.MailViewSet)
router.register(r'OpenModel', viewsets.OpenViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('charts/', views.charts, name='jscharts'),
    path('charts/temperature', views.all_temp_charts, name="all_temp"),
    path('charts/temperature/<str:room>', views.temp_charts, name="temp_charts"),

    path('admin/', admin.site.urls),

    path('upload/temp/', views.post_temp, name='upload_temp'),
    path('upload/water/', views.post_water, name='upload_level'),
    path('upload/waterdetected/', views.post_water_detected, name='upload_detected'),
    path('upload/mail/', views.post_mail, name='upload_mail'),

    path(r'api/', include(router.urls)),
    path(r'api/room/<str:room>',endpoints.str_test, name='str_test'),
    path(r'api/temperatures/<str:room>', endpoints.last_temp, name='api_temp'),
    path(r'api/water', endpoints.water_level, name='api_water'),
    path(r'api/mail', endpoints.mail_delivered, name='api_mail'),
    path(r'api/detection', endpoints.water_detection, name="api_detected"),
    path(r'api/temperatures/<str:room>/<int:datapoints>', endpoints.temp_chart_by_room, name="api_temp2")
]
