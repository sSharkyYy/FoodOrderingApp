from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView

from FoodOrdering.Forms.AddDishForm import AddDishForm
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Dish, RestaurantProfile, Types


class AddDish(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    def has_permission(self):
        try:
            ProfileService.get_restaurant_profile(self.request.user)
        except RestaurantProfile.DoesNotExist:
            return False
        return True

    model = Dish
    template_name = 'FoodOrdering/Restaurant/Dishes/add.html'
    form_class = AddDishForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['type'].queryset = Types.objects.filter(
            owner=ProfileService.get_restaurant_profile(self.request.user))
        return form

    def form_valid(self, form):
        self.object: Dish = form.save(commit=False)
        self.object.restaurant: RestaurantProfile = ProfileService.get_restaurant_profile(self.request.user)

        return super().form_valid(form)

    def get_success_url(self):
        return '/'
