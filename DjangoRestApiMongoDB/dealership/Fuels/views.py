from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dealership.models import CarType, Fuel, Brand, CarModel
from dealership.serializers import CarTypeSerializer, FuelSerializer, BrandSerializer, CarModelSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def Fuels_list(request):
    if request.method == 'GET':
        fuel = Fuel.objects.all()
        obs = request.GET.get('fuel',None)
        if obs is not None:
            fuel = Fuel.filter(obs__icontains=obs)
        fuel_serializer = FuelSerializer(fuel, many = True)
        return JsonResponse(fuel_serializer.data, safe=False)

    elif request.method == 'POST':
        fuel_data = JSONParser().parse(request)
        fuel_serialized = FuelSerializer(data = fuel_data)
        if fuel_serialized.is_valid():
            fuel_serialized.save()
            return JsonResponse(fuel_serialized.data, status = status.HTTP_201_CREATED)
        return JsonResponse(fuel_serialized.errors, status = status.HTTP_406_NOT_ACCEPTABLE)

