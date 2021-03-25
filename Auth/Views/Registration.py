from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views import View

from Auth.Forms.RegisterForm import RegisterForm
from Auth.models import User
from Auth.services.UserService import UserService


class Registration(View):
    def get(self, request, *args, **kwargs):
        try:
            user_type = User.UserTypes(kwargs.get('user_type', None))
        except ValueError:
            return HttpResponseBadRequest()

        form = RegisterForm.get_form(user_type.value)()
        return render(request, 'Auth/register.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        try:
            user_type = User.UserTypes(kwargs.get('user_type', None))
        except ValueError:
            return HttpResponseBadRequest()

        form = RegisterForm.get_form(user_type.value)(request.POST)
        if not form.is_valid():
            return render(request, 'Auth/register.html', context={'form': form})

        UserService().create_user(user_type=user_type.value, **form.cleaned_data)
        return render(request, 'Auth/register.html', context={'form': form})
