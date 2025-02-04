from django.db import models

# Create your models here.

class SensorData(models.Model):
    valve = models.ForeignKey("valve",on_delete=models.CASCADE, limit_choices_to={"valve_no__in": [1, 2]},)
    timestamp = models.DateTimeField(auto_now=True),
    moisture = models.IntegerField()
    tank_level = models.DecimalField(max_digits=8, decimal_places=2)
    temperature = models.DecimalField(max_digits=8,decimal_places=2)
    valve_open_time = models.DateTimeField(auto_now_add=True)
    valve_close_time = models.DateTimeField(auto_now_add=True)

class Valve(models.Model):
    valve_no = models.IntegerField(blank=False,choices=[
            (1, 'Valve 1'),
            (2, 'Valve 2')
        ],
        error_messages={
            'invalid_choice': 'Valve number must be either 1 or 2'
        })
    opening_time = models.DateTimeField(auto_now_add=True)
    tank_level = models.DecimalField(max_digits=8, decimal_places=2)
    flow_rate = models.DecimalField(max_digits=8, decimal_places=2)
    soil_moisture = models.IntegerField()
    soil_temperature = models.DecimalField(max_digits=8, decimal_places=2)
    closing_time =models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True),



