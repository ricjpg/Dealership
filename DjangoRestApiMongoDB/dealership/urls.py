from django.urls import re_path
from dealership.CarModels.views import CarModels_view, CarModels_list
from dealership.CarType.views import CarType_list, CarType_details
from dealership.Fuels.views import Fuels_list
from dealership.Brands.views import Brands_list
from dealership.Transmissions.views import Transmissions_list
from dealership.Colors.views import Color_list
from dealership.modelVersion.views import ModelVersions_list
from dealership.Cars.views import Cars_list

urlpatterns = [
    re_path(r'^api/CarTypes$', CarType_list),
    re_path(r'^api/CarTypes/(?P<pk>[0-9]+)$', CarType_details),

    re_path(r'^api/Fuels$', Fuels_list),
    re_path(r'^api/Brands$', Brands_list),
    re_path(r'^api/CarModels$', CarModels_list),
    re_path(r'^api/Transmissions$',Transmissions_list),
    re_path(r'^api/Colors$', Color_list),
    re_path(r'^api/CarModels$', CarModels_view),
    re_path(r'^api/ModelVersions$', ModelVersions_list),
    re_path(r'^api/Cars$', Cars_list)
    
]



