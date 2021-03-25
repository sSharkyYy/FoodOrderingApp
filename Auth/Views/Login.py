from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic.base import View

from Auth.Forms.LoginForm import LoginForm


class Login(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'Auth/login.html', {'form': LoginForm()})

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)

        if not login_form.is_valid():
            return render(request, 'Auth/login.html', {'form': login_form})

        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            messages.error(request, 'Invalid credentials')
            return redirect('Auth:login')

        messages.success(request, 'Successful login')
        login(request=request, user=user)
        return redirect('/')
