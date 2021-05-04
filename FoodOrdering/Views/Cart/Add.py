from django.db import transaction
from django.utils import timezone
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from personal.models import Dish, Cart


class AddToCart(View):

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        dish = kwargs.get('dish')
        quantity = request.GET.get('quantity', None)
        if quantity is not None:
            try:
                quantity = int(quantity)
            except TypeError:
                return HttpResponse('Invalid quantity', status=400)

        dish = get_object_or_404(Dish, pk=dish)

        if not dish.restaurant.is_open():
            print('Is_open', dish.restaurant.is_open())
            return HttpResponse('Restaurant is closed', status=400)

        cart = Cart.get_cart(request.user, request.session.session_key)
        try:
            cart.add_dish(dish, quantity)
        except Cart.MultipleRestaurantInCartError:
            return HttpResponse('Egyszerre csak 1 étteremből rendelhetsz.', status=400)

        return HttpResponse('OK')
