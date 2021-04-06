from django.core.exceptions import ValidationError
from django.urls import reverse
from django.views.generic import CreateView

from FoodOrdering.Forms.AddCategories import AddCategoriesForm
from FoodOrdering.services.TypeService import TypeService
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Types, RestaurantProfile


class AddType(CreateView):
    model = Types
    template_name = 'FoodOrdering/Restaurant/Types/Add.html'
    form_class = AddCategoriesForm
    # success_url = reverse('FoodOrdering:list_types')

    def form_valid(self, form):
        self.object: Types = form.save(commit=False)
        self.object.owner: RestaurantProfile = ProfileService.get_restaurant_profile(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('FoodOrdering:list_types')
