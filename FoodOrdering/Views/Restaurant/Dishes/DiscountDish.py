from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic import View

from FoodOrdering.Forms.SetDiscount import SetDiscountforDish, SetDiscountforStyle, SetDiscountforType
from FoodOrdering.services.DishService import DishService
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Dish


class DiscountDish(View):
    def get(self, request, *args, **kwargs):
        form1 = SetDiscountforDish()
        dishes = DishService.get_dishes(ProfileService.get_restaurant_profile(request.user))
        # form2 = SetDiscountforType()
        # form3 = SetDiscountforStyle()
        return render(request, 'FoodOrdering/Restaurant/Dishes/discount_dishes.html',
                      {'form1': form1, 'dishes': dishes})

    def post(self, request, *args, **kwargs):
        form1 = SetDiscountforDish(request.POST)
        values = [x for x in request.POST if str(x).find('dish-') != -1]
        values = [int(str(x).split('-')[1]) for x in values if request.POST[x]]
        print(type(values))
        if form1.is_valid():
            discount_price = form1.cleaned_data.get('discount_price', None)
            start_date = form1.cleaned_data.get('discount_start_date', None)
            end_date = form1.cleaned_data.get('discount_end_date', None)
            if discount_price is not None:
                Dish.objects.filter(pk__in=values).update(discount_price=discount_price, discount_start_date=start_date, discount_end_date=end_date)
        return redirect('/')
