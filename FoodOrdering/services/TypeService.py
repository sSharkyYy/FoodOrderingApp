from Auth.models import User
from personal.models import Types


class TypeService:

    @staticmethod
    def get_restaurant_profile(user: User):
        return Types.objects.all()
