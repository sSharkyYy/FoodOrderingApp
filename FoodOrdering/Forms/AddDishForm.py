from django.forms import ModelForm

from personal.models import Dish


class AddDishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ['restaurant', ]
