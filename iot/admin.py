from django.contrib import admin

from iot.models import SensorData, Valve, ValveControl

# Register your models here.
admin.site.register(SensorData)
admin.site.register(Valve)
admin.site.register(ValveControl)