from rest_framework import serializers
from .models import *


class SensorDataSerializer(serializers.ModelSerializer):
      class Meta:
            model = SensorData
            fields = '__all__'
            

class ValveSerializer(serializers.ModelSerializer):
      class Meta:
            model = Valve
            fields =['id', 'timestamp']
      def validate_valve_no(self, value):
        if value not in [1, 2]:
            raise serializers.ValidationError("Valve number must be either 1 or 2")
        return value
      
class ValveControlSerializer(serializers.ModelSerializer):
     class Meta:
          model = ValveControl
          fields = '__all__'