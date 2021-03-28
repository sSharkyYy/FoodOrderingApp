from Auth.models import User
from personal.models import RestaurantProfile


class ProfileService:

    @staticmethod
    def get_restaurant_profile(user: User):
        return RestaurantProfile.objects.get(user=user)
