from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dealership.models import CarVersion
from dealership.serializers import VersionSerializer, VersionViewSerializer
from rest_framework.decorators import api_view

    
@api_view(['GET','POST'])
def ModelVersions_list(request):
    if request.method == 'GET':
        carmodel = CarVersion.objects.all()
        obs = request.GET.get('version',None)
        if obs is not None:
            carmodel = CarVersion.filter(obs__icontains=obs)
        carmodel_serializer = VersionViewSerializer(carmodel, many = True)
        return JsonResponse(carmodel_serializer.data, safe = False)
        

    elif request.method == 'POST':
        model_data = JSONParser().parse(request)
        model_serialized = VersionSerializer(data=model_data)
        if model_serialized.is_valid():
            model_serialized.save()
            return JsonResponse(model_serialized.data, status=status.HTTP_201_CREATED)
        return JsonResponse(model_serialized.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
@api_view(['GET','DELETE','POST'])
def ModelVersions_view(request):
    if request.method == 'GET':
        carmodel = CarVersion.objects.all()
        obs = request.GET.get('version',None)
        if obs is not None:
            carmodel = CarVersion.filter(obs__icontains=obs)
        carmodel_serializer = VersionViewSerializer(carmodel, many = True)
        return JsonResponse(carmodel_serializer.data, safe = False)


