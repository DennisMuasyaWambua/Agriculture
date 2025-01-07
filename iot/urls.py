from django.urls import path
from .views import *

urlpatterns = [
    path("sensordata/", SensorDataView.as_view(), name="sensor data"),
    path("valve/", ValveView.as_view(), name="valve")
]