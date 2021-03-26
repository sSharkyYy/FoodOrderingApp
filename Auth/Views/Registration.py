from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views import View

from Auth.Forms.RegisterForm import RegisterForm
from Auth.models import User
from Auth.services.UserService import UserService


class Registration(View):
    def get(self, request, *args, **kwargs):
        try:
            user_type = User.UserTypes[kwargs.get('user_type', None).upper()]
        except KeyError:
            return HttpResponseBadRequest()

        form = RegisterForm.get_form(user_type.name)()
        return render(request, 'Auth/registration.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        try:
            user_type = User.UserTypes[kwargs.get('user_type', None).upper()]
        except KeyError or AttributeError:
            return HttpResponseBadRequest()

        form = RegisterForm.get_form(user_type.name)(request.POST)
        if not form.is_valid():
            return render(request, 'Auth/registration.html', context={'form': form})

        try:
            UserService.create_user(user_type=user_type.name, **form.cleaned_data)
        except Exception as e:
            raise e

        return render(request, 'Auth/registration.html', context={'form': form})
