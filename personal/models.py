from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Styles(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Types(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('FoodOrdering:edit_categories', kwargs={'pk': self.pk})


class Allergen(models.Model):
    allergen = models.CharField(max_length=50)

    def __str__(self):
        return self.allergenfree


class DishAndAllergen(models.Model):
    allergen = models.ManyToManyField('Allergen', blank=True)
    dish = models.ManyToManyField('Dish', blank=True)

    def __str__(self):
        return self.allergen + self.dish


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    cityID = models.ForeignKey('City', on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CustomerProfile(Profile):
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)


class CourierProfile(Profile):
    divident = models.IntegerField
    phone_number = models.CharField(max_length=10)
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()


class RestaurantProfile(Profile):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    styleID = models.ForeignKey('Styles', on_delete=models.CASCADE)
    openTime = models.CharField(max_length=50)


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.ForeignKey('Types', on_delete=models.CASCADE)
    style = models.ForeignKey('Styles', on_delete=models.CASCADE)
    price = models.IntegerField()
    restaurant = models.ForeignKey('RestaurantProfile', on_delete=models.CASCADE)
    discount_price = models.IntegerField(blank=True, null=True)
    discount_start_date = models.DateField(blank=True, null=True)
    discount_end_date = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to='dishes/')

    def get_price(self):
        if self.discount_price is None:
            return self.price
        now = timezone.now()
        # Akciós időszak
        if self.discount_start_date < now and self.discount_end_date > now:
            return self.discount_price
        return self.price

    def __str__(self):
        return self.name
