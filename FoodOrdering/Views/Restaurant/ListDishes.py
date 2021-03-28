from django.core.paginator import Paginator
from django.views.generic import DetailView

from Auth.models import User
from FoodOrdering.services.DishService import DishService
from personal.models import Dish


class ListDishes(DetailView):
    model = User
    queryset = model.objects.prefetch_related('dishes').select_related('RestaurantProfile')

    def get_context_data(self, **kwargs):
        self.object: User = self.get_object()

        dishes = DishService.get_dishes()
        pagination_count, paginator = self.get_pagination(dishes)
        return self.create_dish_context(kwargs, pagination_count, paginator)

    def create_dish_context(self, kwargs, pagination_count, paginator):
        context = super().get_context_data(**kwargs)
        context['dishes'] = paginator
        context["pagination_count"] = pagination_count
        return context

    def get_pagination(self, dishes):
        page_number = self.request.GET.get('page', None)
        pagination_count = self.request.GET.get('pagination_count', 30)
        if not str(pagination_count).isnumeric() or int(pagination_count) < 1:
            pagination_count = 30
        paginator = Paginator(dishes, pagination_count).get_page(page_number)
        return pagination_count, paginator
