from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from personal.models import Cart


class ClearCart(View):
    def get(self, request, *args, **kwargs):
        cart = Cart.get_cart(request.user, request.session.session_key)
        cart.delete()
        messages.success(request, 'Kosár tartalma sikeresen törölve')
        return redirect('/')
