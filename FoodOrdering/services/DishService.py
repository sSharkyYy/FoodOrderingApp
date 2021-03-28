from personal.models import Dish, Types


class DishService:

    @staticmethod
    def get_dishes(restaurant_profile=None):
        qs = Dish.objects.select_related('type').select_related('style')
        if restaurant_profile is None:
            return qs
        return qs.filter(restaurant=restaurant_profile.pk)

    @staticmethod
    def get_dish_categories(restaurant_profile=None):
        qs = Types.objects.select_related('owner').prefetch_related('dish_set')
        if restaurant_profile is None:
            return qs
        return qs.filter(owner=restaurant_profile.pk)
