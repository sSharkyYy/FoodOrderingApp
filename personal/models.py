from django.db import models


class Styles(models.Model):
    name = models.CharField(max_length=50)


class Types(models.Model):
    name = models.CharField(max_length=50)


class AllergenFree(models.Model):
    allergenfree = models.CharField(max_length=50)


class City(models.Model):
    name = models.CharField(max_length=50)


class Customer(models.Model):
    name = models.CharField(max_length=50)
    cityID = models.ForeignKey('City', on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    password = models.CharField


class Delivery(models.Model):
    name = models.CharField(max_length=50)
    cityID = models.ForeignKey('City', on_delete=models.CASCADE)
    divident = models.IntegerField
    phone_number = models.CharField(max_length=10)
    delivery_time_frame = models.CharField(max_length=50)
    password = models.CharField


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    cityID = models.ForeignKey('City', on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    styleID = models.ForeignKey('Styles', on_delete=models.CASCADE)
    openTime = models.CharField(max_length=50)
    password = models.CharField


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    TypeID = models.ForeignKey('Types', on_delete=models.CASCADE)
    StyleID = models.ForeignKey('Styles', on_delete=models.CASCADE)
    Price = models.IntegerField
    RestaurantID = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    discount_price = models.IntegerField
    discount_end_date = models.DateField
    allergenfreeID = models.ForeignKey('Allergenfree', on_delete=models.CASCADE)
    picture = models.CharField
