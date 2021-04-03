from Auth.models import User, UserTypes


class UserService:

    @staticmethod
    def create_user(user_type: str, **kwargs):
        user_type = UserTypes[user_type.upper()]
        kwargs['tenant_type'] = user_type.value
        method = UserService.__dict__.get(f'_UserService__create_{user_type.name.lower()}')
        method.__get__(UserService)(**kwargs)

    @staticmethod
    def __create_restaurant(email, password, first_name, last_name, tenant_type, **kwargs):
        User.objects.create_user(
            email,
            password,
            first_name,
            last_name,
            tenant_type=tenant_type,
        )

    @staticmethod
    def __create_customer(email, password, nickname, first_name, last_name, tenant_type, **kwargs):
        print(kwargs)
        User.objects.create_user(
            email=email,
            password=password,
            nickname=nickname,
            first_name=first_name,
            last_name=last_name,
            tenant_type=tenant_type
        )

    @staticmethod
    def __create_courier(email, password, first_name, last_name, tenant_type, **kwargs):
        User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            tenant_type=tenant_type
        )

    @staticmethod
    def user_exists(email_address: str):
        try:
            User.objects.get(email=email_address)
        except Exception as e:
            return False
        return True
