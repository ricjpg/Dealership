from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dealership.models import Brand
from dealership.serializers import BrandSerializer
from rest_framework.decorators import api_view



@api_view(['GET','POST','DELETE'])
def Brands_list(request):
    if request.method == 'GET':
        brand = Brand.objects.all()
        obs = request.GET.get('brand_name',None)
        if obs is not None:
            brand = Brand.filter(obs__icontains=obs)
        brand_serializer = BrandSerializer(brand, many = True)
        return JsonResponse(brand_serializer.data, safe=False)
    
    elif request.method == 'POST':
        brand_data = JSONParser().parse(request)
        brand_serializer = BrandSerializer(data=brand_data)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return JsonResponse(brand_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(brand_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    elif request.method == 'DELETE':
        count = Brand.objects.all().delete()
        return JsonResponse({'message': '{} Fuel type were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    