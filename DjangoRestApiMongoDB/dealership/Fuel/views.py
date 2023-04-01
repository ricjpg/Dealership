from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dealership.models import Fuel
from dealership.serializers import FuelSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def Fuel_list(request):
    if request.method == 'GET':
        fuel = Fuel.objects.all()
        fuel_data = request.GET.get('Color',None)
        if fuel_data is not None:
            fuel = Fuel.filter(fuel_data__icontains=fuel_data)
        fuel_data = FuelSerializer(fuel, many = True)
        return JsonResponse(fuel_data.data, safe=False)
    
    elif request.method == 'POST':
        fuel_data = JSONParser().parse(request)
        fuel_serialized = FuelSerializer(data=fuel_data)
        if fuel_serialized.is_valid():
            fuel_serialized.save()
            return JsonResponse(fuel_serialized.data, status=status.HTTP_201_CREATED)
        return JsonResponse(fuel_serialized.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    