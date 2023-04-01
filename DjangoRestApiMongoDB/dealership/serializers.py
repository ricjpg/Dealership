from rest_framework import serializers
from dealership.models import CarType, Brand, CarColor, CarStatus, Transmission, Fuel, CarModel, CarVersion, Cars

class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = (
            'id',
            'car_type'
        )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'brand_name',
        )


class CarColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarColor
        fields = (
            'id',
            'color'
        )


class CarStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarStatus
        fields = (
            'id',
            'status'
        )


class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = (
            'id',
            'type_transmission'
        )







class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = (
            'id',
            'fuel'
        )

class CarModelSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    # cartype = CarTypeSerializer()
    class Meta:
        model = CarModel
        fields = (
            'id',
            'brand',
            'cartype',
            'model_name'
        )

class ModelViewSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    cartype = CarTypeSerializer()
    class Meta:
        model = CarModel
        fields = (
            'id',
            'brand',
            'cartype',
            'model_name'
        )


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarVersion
        fields = (
            'id',
            'model',
            'model_version'
        )
        # depth = 1

class VersionViewSerializer(serializers.ModelSerializer):
    # carModel = VersionSerializer()
    class Meta:
        model = CarVersion
        fields = (
            'id',
            'model',
            'model_version'
        )
        depth=2

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = (
            'id',
            'type',
            'brand',
            'model',
            'version',
            'transmission',
            'color',
            'isUsed'
        )

class CarsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = (
            'id',
            'type',
            'brand',
            'model',
            'version',
            'transmission',
            'color',
            'isUsed'
        )
        depth = 2