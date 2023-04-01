from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dealership.models import Transmission
from dealership.serializers import TransmissionSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def Transmissions_list(request):
    if request.method == 'GET':
        transmission = Transmission.objects.all()
        type_t = request.GET.get('type_transmissions',None)
        if type_t is not None:
            transmission = Transmission.filter(type_t__icontains=type_t)
        type_serialized = TransmissionSerializer(transmission, many = True)
        return JsonResponse(type_serialized.data, safe=False)
    
    elif request.method == 'POST':
        type_data = JSONParser().parse(request)
        type_serialized = TransmissionSerializer(data=type_data)
        if type_serialized.is_valid():
            type_serialized.save()
            return JsonResponse(type_serialized.data, status=status.HTTP_201_CREATED)
        return JsonResponse(type_serialized.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    