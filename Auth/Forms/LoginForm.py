from django.forms import Form, EmailField, CharField, PasswordInput


class LoginForm(Form):
    email = EmailField(required=True)
    password = CharField(required=True, max_length=255, widget=PasswordInput)
