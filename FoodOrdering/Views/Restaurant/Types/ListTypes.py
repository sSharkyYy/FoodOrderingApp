from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import ListView

from FoodOrdering.services.DishService import DishService
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Types


class ListTypes(LoginRequiredMixin, ListView):
    model = Types
    template_name = 'FoodOrdering/Restaurant/Types/list_types.html'
    context_object_name = 'types'

    def get_queryset(self):
        return super().get_queryset().filter(owner=ProfileService.get_restaurant_profile(self.request.user))
