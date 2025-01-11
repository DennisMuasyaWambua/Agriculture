from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic.list import ListView
from rest_framework import status
from .models import *
from .serializer import SensorDataSerializer, ValveSerializer
from rest_framework.response import Response



# Create your views here.
class SensorDataView(APIView):
    serializer_class = SensorDataSerializer;
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': 'Invalid data provided',
                'error': serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        moisture = data.get('moisture')
        tank_level = data.get('tank_level')
        temperature = data.get('temperature')
        valve_open_time = data.get('valve_open_time')
        valve_close_time = data.get('valve_close_time')
        valve = data.get('valve')
        print(valve)
        valve_instance = Valve.objects.filter(id=valve).first()
        sensor_data = SensorData(valve=valve_instance, moisture=moisture, tank_level=tank_level, temperature = temperature, valve_open_time = valve_open_time, valve_close_time=valve_close_time)
        sensor_data.save()
        return Response({
            'status': True,
            'message': 'sensor data saved successfully',
        },status=status.HTTP_200_OK)
    
class GetSensorData(APIView):
    def get(self, request):
        sensors_data = SensorData.objects.all()
        serializer = SensorDataSerializer(sensors_data, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ValveView(APIView):
    serializer_class = ValveSerializer
    
    def post(self, request):
        try:
            # Convert request data to proper format
            data = {
                'valve_no': int(request.data.get('valve_no')),
                'tank_level': float(request.data.get('tank_level')),
                'flow_rate': float(request.data.get('flow_rate')),
                'soil_moisture': int(request.data.get('soil_moisture')),
                'soil_temperature': float(request.data.get('soil_temperature')),
                'is_open': bool(request.data.get('is_open'))
            }
            
            # Handle opening_time and closing_time only if they're provided
            if request.data.get('opening_time'):
                data['opening_time'] = str(request.data.get('opening_time'))
            if request.data.get('closing_time'):
                data['closing_time'] = str(request.data.get('closing_time'))
            
            serializer = self.serializer_class(data=data)
            if not serializer.is_valid():
                return Response({
                    'status': False,
                    'message': 'Invalid data provided',
                    'error': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
                
            serializer.save()
            return Response({
                'status': True,
                'message': 'Valve data saved successfully'
            }, status=status.HTTP_200_OK)
            
        except (ValueError, TypeError) as e:
            return Response({
                'status': False,
                'message': 'Data type conversion error',
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
    # def get(self, request):
    #     valve_data = Valve.objects.all()
    #     serializer = ValveSerializer(valve_data, many=True)
    #     return Response({
    #         serializer.data
    #     })
class GetValveVeiw(APIView):
    def get(self, request):
        valve_data = Valve.objects.all()
        serializer = ValveSerializer(valve_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        