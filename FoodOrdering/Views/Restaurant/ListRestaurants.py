from django.views.generic import ListView

from Auth.models import User, UserTypes
from personal.models import RestaurantProfile


class ListRestaurants(ListView):
    model = RestaurantProfile
    template_name = 'FoodOrdering/index.html'

    def get_queryset(self):
        return super().get_queryset().filter(user__tenant_type=UserTypes.RESTAURANT.value).select_related('user')
