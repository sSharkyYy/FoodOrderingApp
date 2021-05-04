from django.views.generic import ListView

from personal.models import DishToCart, Cart


class ListCartItems(ListView):
    model = DishToCart
    template_name = 'FoodOrdering/Cart/cart.html'

    def get_queryset(self):
        cart = Cart.get_cart(self.request.user, self.request.session.session_key)
        qs = DishToCart.objects.filter(cart=cart).select_related('dish')
        return qs
