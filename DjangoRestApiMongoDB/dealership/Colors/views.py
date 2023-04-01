from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dealership.models import CarColor
from dealership.serializers import CarColorSerializer
from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def Color_list(request):
    if request.method == 'GET':
        color = CarColor.objects.all()
        color_car = request.GET.get('Color',None)
        if color_car is not None:
            color = CarColor.filter(color_car__icontains=color_car)
        color_car = CarColorSerializer(color, many = True)
        return JsonResponse(color_car.data, safe=False)
    
    elif request.method == 'POST':
        car_color = JSONParser().parse(request)
        color_serialized = CarColorSerializer(data=car_color)
        # color_check = CarColor.objects.filter(color = car_color['color'])
        # if len(color_check)>0:
        #     return JsonResponse({'Color already exists'},status=status.HTTP_406_NOT_ACCEPTABLE) 
        if color_serialized.is_valid():
            color_serialized.save()
            return JsonResponse(color_serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(color_serialized.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    