from django.urls import path
from . import views

urlpatterns = [
    path('', views.charts, name='jscharts'),
    path('temperature/', views.all_temp_charts, name="all_temp"),
    path('temperature/<str:room>', views.temp_charts, name="temp_charts"),
    path('temperaturetest/<str:room>', views.temptest_charts, name="temptest_charts"),
]
