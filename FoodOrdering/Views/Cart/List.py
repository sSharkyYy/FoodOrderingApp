from django.views.generic import ListView

from personal.models import DishToCart, Cart


class ListCartItems(ListView):
    model = DishToCart
    template_name = 'FoodOrdering/Cart/cart.html'

    def get_queryset(self):
        qs = super().get_queryset()
        cart = Cart.get_cart(self.request.user, self.request.session.session_key)
        qs.filter(cart=cart).select_related('dish')
        return qs
