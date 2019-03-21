from . import endpoints
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'TempModel', viewsets.TempViewSet)
router.register(r'WaterModel', viewsets.WaterViewSet)
router.register(r'DetectionModel', viewsets.DetectionViewSet)
router.register(r'MailModel', viewsets.MailViewSet)
router.register(r'OpenModel', viewsets.OpenViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/room/<str:room>',endpoints.str_test, name='str_test'),
    path(r'api/temperatures/<str:room>', endpoints.last_temp, name='api_temp'),
    path(r'api/water', endpoints.water_level, name='api_water'),
    path(r'api/mail', endpoints.mail_delivered, name='api_mail'),
    path(r'api/detection', endpoints.water_detection, name="api_detected"),
    path(r'api/temperatures/<str:room>/<int:datapoints>', endpoints.temp_chart_by_room, name="api_temp2")
]
