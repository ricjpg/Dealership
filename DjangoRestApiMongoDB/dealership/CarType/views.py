from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dealership.models import CarType
from dealership.serializers import CarTypeSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST','DELETE'])
def CarType_list(request):
    if request.method == 'GET':
        cartype = CarType.objects.all()
        obs = request.GET.get('car_type',None)
        if obs is not None:
            cartype = CarType.filter(obs__icontains=obs)
        cartype_serializer = CarTypeSerializer(cartype, many = True)
        return JsonResponse(cartype_serializer.data, safe=False)
    
    elif request.method == 'POST':
        cartype_data = JSONParser().parse(request)
        cartype_serializer = CarTypeSerializer(data=cartype_data)
        if cartype_serializer.is_valid():
            cartype_serializer.save()
            return JsonResponse(cartype_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cartype_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    elif request.method == 'DELETE':
        count = CarType.objects.all().delete()
        return JsonResponse({'message': '{} Car Types were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','PUT','DELETE'])
def CarType_details(request, pk):
    try:
        cartype = CarType.objects.get(pk=pk)
    except CarType.DoesNotExist:
        return JsonResponse({'message': 'Car Type does not exist!'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        cartype_serializer = CarTypeSerializer(cartype)
        return JsonResponse(cartype_serializer.data)
    
    elif request.method == 'PUT':
        cartype_data = JSONParser().parse(request)
        cartype_serializer = CarTypeSerializer(cartype, data = cartype_data)
        if cartype_serializer.is_valid():
            cartype_serializer.save()
            return JsonResponse(cartype_serializer.data)
        return JsonResponse(cartype_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cartype.delete()
        return JsonResponse({'message': '{} Car Type were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)