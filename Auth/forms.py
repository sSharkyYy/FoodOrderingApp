from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.forms import Form, EmailField, CharField, PasswordInput
from django.shortcuts import redirect, render


class LoginForm(Form):
    email = EmailField(required=True)
    password = CharField(required=True, max_length=255, widget=PasswordInput)


