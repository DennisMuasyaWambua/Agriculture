from django.urls import path
from .views import *

urlpatterns = [
    path("sensordata/", SensorDataView.as_view(), name="sensor data"),
    path("valve/", ValveView.as_view(), name="valve"),
    path("getsensordata/", GetSensorData.as_view(), name="getsensordata"),
    path("getvalvedata/",GetValveVeiw.as_view(), name="getvalvedata"),
    path("valveControl/", ValveControlView.as_view(), name="valve")
]   