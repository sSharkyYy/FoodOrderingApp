from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import logout


class Logout(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('/')
