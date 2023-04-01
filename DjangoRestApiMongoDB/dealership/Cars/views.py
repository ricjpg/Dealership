from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dealership.models import Cars
from dealership.serializers import CarsSerializer, CarsViewSerializer
from rest_framework.decorators import api_view

    
@api_view(['GET','POST'])
def Cars_list(request):
    if request.method == 'GET':
        cars_data = Cars.objects.all()
        obs = request.GET.get('isUsed',None)
        if obs is not None:
            cars_data = Cars.filter(obs__icontains=obs)
        cars_data_serializer = CarsViewSerializer(cars_data, many = True)
        return JsonResponse(cars_data_serializer.data, safe = False)
        

    elif request.method == 'POST':
        cars_data = JSONParser().parse(request)
        cars_serialized = CarsSerializer(data=cars_data)
        if cars_serialized.is_valid():
            cars_serialized.save()
            return JsonResponse(cars_serialized.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cars_serialized.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    

