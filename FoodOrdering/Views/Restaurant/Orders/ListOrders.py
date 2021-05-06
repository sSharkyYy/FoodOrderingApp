from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Order, RestaurantProfile, OrderStatus


class ListOrders(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    def has_permission(self):
        try:
            self.restaurant = ProfileService.get_restaurant_profile(self.request.user)
            return True
        except RestaurantProfile.DoesNotExist:
            return False

    model = Order
    template_name = 'FoodOrdering/Restaurant/Orders/list_orders.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(cart__restaurant=self.restaurant).exclude(status=OrderStatus.Delivered.value)
