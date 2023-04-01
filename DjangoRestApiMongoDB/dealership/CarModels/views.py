from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from dealership.models import CarType, Fuel, Brand, CarModel
from dealership.serializers import CarTypeSerializer, FuelSerializer, BrandSerializer, CarModelSerializer, ModelViewSerializer
from rest_framework.decorators import api_view

    
@api_view(['GET','DELETE','POST'])
def CarModels_list(request):
    if request.method == 'GET':
        carmodel = CarModel.objects.all()
        obs = request.GET.get('model_name',None)
        if obs is not None:
            carmodel = CarModel.filter(obs__icontains=obs)
        carmodel_serializer = ModelViewSerializer(carmodel, many = True)
        return JsonResponse(carmodel_serializer.data, safe = False)
    
    # elif request.method == 'POST':
    #     carmodel_data = JSONParser().parse(request)
    #     carmodel_serializer = CarModelSerializer(data = carmodel_data)
    #     if carmodel_serializer.is_valid():
    #         carmodel_serializer.save()
    #         return JsonResponse(carmodel_serializer.data, status = status.HTTP_201_CREATED)
    #     return JsonResponse(carmodel_serializer.errors, status = status.HTTP_406_NOT_ACCEPTABLE)
    
    
    
    # if request.method == 'POST':
    #         carmodel = request.data
    #         newModel = CarModel.objects.create(brand=Brand.objects.get(id=carmodel["brand"]), model_name = carmodel["model_name"])
    #         newModelS = CarModelSerializer(data = newModel)
    #         if newModelS.is_valid():
    #             newModelS.save()
    #             return JsonResponse(newModelS.data)
    # return JsonResponse(newModelS.errors, status = status.HTTP_406_NOT_ACCEPTABLE)


#-----------------
    # elif request.method == 'POST':
    #     car_model = JSONParser().parse(request)
    #     new_car_model = CarModel.objects.create(brand = Brand.objects.get(id = car_model["id"]),model_name = car_model["model_name"])
    #     newCarSerializer = CarModelSerializer(data = new_car_model)
    #     if newCarSerializer.is_valid():
    #         newCarSerializer.create()
    #         return JsonResponse(newCarSerializer.data, status = status.HTTP_201_CREATED)
    #     return JsonResponse(newCarSerializer.errors, status = status.HTTP_406_NOT_ACCEPTABLE)
#------------------
    elif request.method == 'POST':
        model_data = JSONParser().parse(request)
        model_serialized = CarModelSerializer(data=model_data)
        if model_serialized.is_valid():
            model_serialized.save()
            return JsonResponse(model_serialized.data, status=status.HTTP_201_CREATED)
        return JsonResponse(model_serialized.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    






    # elif request.method == 'DELETE':
    #     count = CarModel.objects.all().delete()
    #     return JsonResponse({'message': '{} Car Models were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)



#-------------------
# @api_view(['POST'])
# def CarModels_new(request):
#     if request.method == 'POST':
#         car_model = JSONParser().parse(request)
#         new_car_model = CarModel.objects.create(brand = Brand.objects.get(id = car_model["brand"]),model_name = car_model["model_name"])
#         newCarSerializer = CarModelSerializer(data = new_car_model)
#         if newCarSerializer.is_valid():
#             newCarSerializer.create()
#             return JsonResponse(newCarSerializer.data, status = status.HTTP_201_CREATED)
#         return JsonResponse(newCarSerializer.errors, status = status.HTTP_406_NOT_ACCEPTABLE)

#-----------------
        


@api_view(['GET','DELETE','POST'])
def CarModels_view(request):
    if request.method == 'GET':
        carmodel = CarModel.objects.all()
        obs = request.GET.get('model_name',None)
        if obs is not None:
            carmodel = CarModel.filter(obs__icontains=obs)
        carmodel_serializer = CarModelSerializer(carmodel, many = True)
        return JsonResponse(carmodel_serializer.data, safe = False)



