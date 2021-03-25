from Auth.models import User


class UserService:

    def create_user(self, user_type: int, **kwargs):
        user_type = User.UserTypes(user_type).name.lower()
        self.__class__.__dict__.get(f'_UserService__create_{user_type}')(self,**kwargs)

    def __create_restaurant(self, *args, **kwargs):
        pass

    def __create_customer(self, *args, **kwargs):
        pass

    def __create_courier(self, *args, **kwargs):
        pass
