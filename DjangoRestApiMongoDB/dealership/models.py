from django.db import models


class CarType(models.Model):
    car_type = models.CharField(max_length=50,blank=False, default='')
    def __str__(self):
        return self.car_type

class Fuel(models.Model):
    fuel = models.CharField(max_length=50, blank=False, default='')
    def __str__(self):
        return self.fuel

class CarStatus(models.Model):
    status = models.BooleanField(default=True)
    #True means that the car is new, False means that the car is used
    def __str__(self):
        return self.status

class CarColor(models.Model):
    color = models.CharField(max_length=50, blank=False, default='')
    def __str__(self):
        return self.color

class Transmission(models.Model):
    type_transmission = models.CharField(max_length=50, blank=False, default='')
    def __str__(self):
        return self.type_transmission

class Brand(models.Model):
    brand_name = models.CharField(max_length=50, blank=False, default='')
    def __str__(self):
        return self.brand_name

class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    cartype = models.ForeignKey(CarType, on_delete=models.CASCADE, null=True)
    model_name = models.CharField(max_length=50, blank=False, default='')
    #for example: Brand=Honda, CarType=Sedan(4doors), modelName=Accord
    #Or: Brand=Honda, CarType=Coupe(2doors), modelName=Civic
    def __str__(self):
        return self.model_name
    


class CarVersion(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True)

    model_version = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        return self.model_version
    
class Cars(models.Model):
    type = models.ForeignKey(CarType, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True)
    version = models.ForeignKey(CarVersion, on_delete=models.CASCADE, null=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(CarColor, on_delete=models.CASCADE, null=True)
    isUsed = models.BooleanField(default=True)

    def __str__(self):
        return self.model
    

