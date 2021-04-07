from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from personal.models import Dish, Cart


class AddToCart(View):

    def get(self, request, *args, **kwargs):
        dish = kwargs.get('dish')
        quantity = request.GET.get('quantity', None)
        if quantity is not None:
            try:
                quantity = int(quantity)
            except TypeError:
                HttpResponse('Invalid quantity', status=401)

        dish = get_object_or_404(Dish, pk=dish)
        cart = Cart.get_cart(request.user, request.session.session_key)
        cart.add_dish(dish, quantity)

        return HttpResponse('OK')
