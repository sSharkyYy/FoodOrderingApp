from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View

from Auth.Forms.RegisterForm import RegisterForm
from Auth.models import User, UserTypes
from Auth.services.UserService import UserService


class Registration(View):
    def get(self, request, *args, **kwargs):
        try:
            user_type = UserTypes[kwargs.get('user_type', None).upper()]
        except KeyError:
            return HttpResponseBadRequest()

        form = RegisterForm.get_form(user_type.name)()
        return render(request, 'Auth/registration.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        try:
            user_type = UserTypes[kwargs.get('user_type', None).upper()]
        except KeyError or AttributeError:
            return HttpResponseBadRequest()

        form = RegisterForm.get_form(user_type.name)(request.POST)
        if not form.is_valid():
            return render(request, 'Auth/registration.html', context={'form': form})

        try:
            UserService.create_user(user_type=user_type.name, **form.cleaned_data)
        except Exception as e:
            print(e)
            messages.error(request, "Couldn't create user")
            return render(request, 'Auth/registration.html', context={'form': form})

        return redirect('/')
