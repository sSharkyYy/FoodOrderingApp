from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from FoodOrdering.Forms.CreateOrder import CreateOrderForm
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Cart, Order, RestaurantProfile


class CreateOrder(View):
    def get(self, request, *args, **kwargs):
        try:
            form = self.get_initial_form(request.user)
        except ValueError:
            messages.error(request, 'Nem vásárolhatsz')
            return redirect('/')
        return render(request, 'FoodOrdering/checkout.html', {'form': form})

    def get_initial_form(self, user):
        if user.is_authenticated:
            customer_profile = ProfileService.get_customer_profile(user)
            form = CreateOrderForm(initial={'address': customer_profile.address, 'name': user.get_full_name()})
        else:
            form = CreateOrderForm()
        return form

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        cart = Cart.get_cart(request.user, request.session.session_key)
        address = None
        name = None

        if cart.restaurant is None or not cart.restaurant.is_open():
            return

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

        order = Order(name=name, address=address, cart=cart, amount=cart.get_sum())
        order.save()
        cart.set_ordered()

        messages.success(request, 'Sikeres megrendelés!')
        return redirect('/')
