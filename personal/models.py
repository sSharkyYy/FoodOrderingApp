from django.conf import settings
from django.db import models


class Styles(models.Model):
    name = models.CharField(max_length=50)


class Types(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class AllergenFree(models.Model):
    allergenfree = models.CharField(max_length=50)


class City(models.Model):
    name = models.CharField(max_length=50)


class Profile(models.Model):
    class Meta:
        abstract = True


class CustomerProfile(Profile):
    name = models.CharField(max_length=50)
    cityID = models.ForeignKey('City', on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)


class DeliveryProfile(Profile):
    name = models.CharField(max_length=50)
    cityID = models.ForeignKey('City', on_delete=models.CASCADE)
    divident = models.IntegerField
    phone_number = models.CharField(max_length=10)
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()


class RestaurantProfile(Profile):
    name = models.CharField(max_length=50)
    cityID = models.ForeignKey('City', on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    styleID = models.ForeignKey('Styles', on_delete=models.CASCADE)
    openTime = models.CharField(max_length=50)


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    TypeID = models.ForeignKey('Types', on_delete=models.CASCADE)
    StyleID = models.ForeignKey('Styles', on_delete=models.CASCADE)
    Price = models.IntegerField()
    RestaurantID = models.ForeignKey('RestaurantProfile', on_delete=models.CASCADE)
    discount_price = models.IntegerField(blank=True, null=True)
    discount_end_date = models.DateField(blank=True, null=True)
    allergenfreeID = models.ForeignKey('AllergenFree', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='Dishes/')
