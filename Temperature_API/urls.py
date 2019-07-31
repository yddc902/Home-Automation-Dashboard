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

from rest_framework import routers

from api_app import views, viewsets, endpoints
from chart_app import urls
from management_app import urls

router = routers.DefaultRouter()
router.register(r'TempModel', viewsets.TempViewSet)
router.register(r'WaterModel', viewsets.WaterViewSet)
router.register(r'DetectionModel', viewsets.DetectionViewSet)
router.register(r'MailModel', viewsets.MailViewSet)
router.register(r'OpenModel', viewsets.OpenViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('charts/', include('chart_app.urls')),
    path('management/', include('management_app.urls')),
    path('projects/project1', views.project1, name="project1"),
    path('admin/', admin.site.urls),

    #These should be included in the api URLs, will have to keep though for legacy support
    path('upload/temp/', views.post_temp, name='upload_temp'),
    path('upload/water/', views.post_water, name='upload_level'),
    path('upload/waterdetected/', views.post_water_detected, name='upload_detected'),
    path('upload/mail/', views.post_mail, name='upload_mail'),

    #This all needs to be activated in the api_app.URLs
    #path('api/', include('api_app.urls'))
    path(r'api/', include(router.urls)),
    path(r'api/room/<str:room>',endpoints.str_test, name='str_test'),
    path(r'api/temperatures/<str:room>', endpoints.last_temp, name='api_temp'),
    path(r'api/water', endpoints.water_level, name='api_water'),
    path(r'api/mail', endpoints.mail_delivered, name='api_mail'),
    path(r'api/detection', endpoints.water_detection, name="api_detected"),
    path(r'api/temperatures/<str:room>/<int:datapoints>', endpoints.temp_chart_by_room, name="api_temp2")
]
