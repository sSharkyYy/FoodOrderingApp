from Auth.models import User, UserTypes
from personal.models import RestaurantProfile, CustomerProfile


class ProfileService:

    @staticmethod
    def get_restaurant_profile(user: User):
        if not user.is_authenticated:
            raise ValueError('User must be authenticated to have a profile')

        if user.tenant_type != UserTypes.RESTAURANT.value:
            raise ValueError('User is not a restaurant')

        return RestaurantProfile.objects.get(user=user)

    @staticmethod
    def get_customer_profile(user: User):
        if not user.is_authenticated:
            raise ValueError('User must be authenticated to have a profile')
        if user.tenant_type != UserTypes.RESTAURANT.value:
            raise ValueError('User is not a customer')

        return CustomerProfile.objects.get(user=user)
