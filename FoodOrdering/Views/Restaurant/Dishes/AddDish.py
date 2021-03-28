from django.core.exceptions import ValidationError
from django.views.generic import CreateView

from FoodOrdering.Forms.AddDishForm import AddDishForm
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Dish, RestaurantProfile


class AddDish(CreateView):
    model = Dish
    template_name = 'FoodOrdering/Restaurant/Dishes/Add.html'
    form_class = AddDishForm

    def form_valid(self, form):
        self.object: Dish = form.save(commit=False)
        self.object.restaurant: RestaurantProfile = ProfileService.get_restaurant_profile(self.request.user)

        return super().form_valid(form)

    def get_success_url(self):
        return '/'
