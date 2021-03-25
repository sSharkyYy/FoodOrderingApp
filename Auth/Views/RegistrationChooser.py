from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views import View

from Auth.Forms.RegisterForm import RegisterForm
from Auth.models import User
from Auth.services.UserService import UserService


class RegistrationChooser(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Auth/registration_chooser.html')
