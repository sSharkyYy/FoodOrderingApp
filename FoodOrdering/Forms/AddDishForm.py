from django.forms import ModelForm

from personal.models import Dish, Types


class AddDishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ['restaurant', ]
