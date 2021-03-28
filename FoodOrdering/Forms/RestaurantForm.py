from django.forms import ModelForm

from personal.models import RestaurantProfile


class RestaurantForm(ModelForm):
    class Meta:
        model = RestaurantProfile
        exclude = ['user', ]

    field_order = ['name', 'address']
