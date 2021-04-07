from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from FoodOrdering.Forms.AddDishForm import AddDishForm
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Dish, RestaurantProfile, Types


class EditDish(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    def has_permission(self):
        self.object: Dish = self.get_object()
        if not self.request.user.is_authenticated:
            return False

        try:
            if self.object.restaurant != ProfileService.get_restaurant_profile(self.request.user):
                return False
        except RestaurantProfile.DoesNotExist:
            return False

        return True

    model = Dish
    template_name = 'FoodOrdering/Restaurant/Dishes/edit.html'
    form_class = AddDishForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['type'].queryset = Types.objects.filter(
            owner=ProfileService.get_restaurant_profile(self.request.user))
        return form

    def get_success_url(self):
        obj = self.get_object()
        return reverse('FoodOrdering:edit_dish', kwargs={"pk": obj.pk})
