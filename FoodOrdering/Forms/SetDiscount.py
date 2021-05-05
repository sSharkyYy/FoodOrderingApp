from django.forms import ModelForm

from personal.models import Dish, Types


class SetDiscountforDish(ModelForm):
    class Meta:
        model = Dish
        # exclude = ['description', 'type', 'style', 'restaurant', 'price', 'picture', 'allergen', ]
        fields = ('discount_start_date', 'discount_end_date', 'discount_price')


class SetDiscountforType(ModelForm):
    class Meta:
        model = Dish
        # exclude = ['name', 'description', 'style', 'restaurant', 'price', 'picture', 'allergen', ]
        fields = ('type', 'discount_start_date', 'discount_end_date', 'discount_price')


class SetDiscountforStyle(ModelForm):
    class Meta:
        model = Dish
        # exclude = ['name', 'description', 'type', 'restaurant', 'price', 'picture', 'allergen', ]
        fields = ('style', 'discount_start_date', 'discount_end_date', 'discount_price')

