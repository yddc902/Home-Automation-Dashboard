from django.urls import path
from . import views

urlpatterns = [
    path('charts/', views.charts, name='jscharts'),
    path('charts/temperature', views.all_temp_charts, name="all_temp"),
    path('charts/temperature/<str:room>', views.temp_charts, name="temp_charts"),
]
