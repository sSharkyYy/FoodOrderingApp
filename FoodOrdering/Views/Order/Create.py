from django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.views import View

from FoodOrdering.Forms.CreateOrder import CreateOrderForm
from personal.models import Cart, Order


class CreateOrder(View):
    def get(self, request, *args, **kwargs):
        form = CreateOrderForm()
        return render(request, 'FoodOrdering/checkout.html')

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        cart = Cart.get_cart(request.user, request.session.session_key)
        address = None
        name = None

        if not request.user.is_authenticated:
            form = CreateOrderForm(request.POST)
            if form.is_valid():
                address = form.cleaned_data.get('address', None)
                name = form.cleaned_data.get('name', None)
        else:
            name = request.user.get_full_name()
            address = request.user.address

        if address is None:
            messages.error(request, 'Invalid address')
            return render(request, 'FoodOrdering/checkout.html')

        if name is None:
            messages.error(request, 'Invalid name')
            return render(request, 'FoodOrdering/checkout.html')

        order = Order(name=name, address=address, cart=cart)
        order.save()
        cart.set_ordered()
