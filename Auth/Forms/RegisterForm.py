from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from django.core.exceptions import ValidationError
from django.forms import Form, EmailField, CharField, PasswordInput

from Auth.models import User
from Auth.services.UserService import UserService


class RegisterForm:

    @staticmethod
    def get_form(user_type: str):
        user_type = User.UserTypes[user_type].name.lower()

        form = RegisterForm.__dict__.get(f'_RegisterForm__{user_type.capitalize()}Form')

        # Default
        if form is None:
            form = RegisterForm.__CustomerForm
        return form

    class __BaseForm(Form):
        email = EmailField(required=True)
        password = CharField(required=True, max_length=255, widget=PasswordInput,
                             help_text=password_validators_help_text_html())
        new_password = CharField(required=True, max_length=255, widget=PasswordInput,
                                 help_text=password_validators_help_text_html())

        def clean_email(self):
            email = self.cleaned_data.get('email', None)
            if UserService.user_exists(email):
                raise ValidationError('Account already exists with given e-mail')
            return email

        def clean_password(self):
            password = self.cleaned_data.get('password', None)
            validate_password(password)
            return password

        def clean(self):
            results = super().clean()
            password = results.get('password', None)
            new_password = results.get('new_password', None)
            if password != new_password:
                raise ValidationError('Passwords must match!')
            return results

    class __RestaurantForm(__BaseForm):
        pass

    class __CustomerForm(__BaseForm):
        nickname = CharField(max_length=254)

    class __CourierForm(__BaseForm):
        pass
