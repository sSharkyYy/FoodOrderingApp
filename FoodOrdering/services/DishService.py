from personal.models import Dish


class DishService:

    @staticmethod
    def get_dishes(restaurant_profile=None):
        qs = Dish.objects.select_related('TypeID').select_related('StyleID')
        if restaurant_profile is None:
            return qs
        return qs.filter(RestaurantID=restaurant_profile.pk)
