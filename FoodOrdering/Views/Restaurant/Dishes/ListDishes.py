from django.views.generic import DetailView

from FoodOrdering.services.DishService import DishService
from personal.models import RestaurantProfile


class ListDishes(DetailView):
    model = RestaurantProfile
    queryset = model.objects.prefetch_related('dish_set')

    template_name = 'FoodOrdering/Restaurant/Dishes/list_dishes.html'

    def get_context_data(self, **kwargs):
        self.object: RestaurantProfile = self.get_object()

        context = super().get_context_data()
        context['dish_categories'] = DishService.get_dish_categories(self.object)
        print(context)
        return context
