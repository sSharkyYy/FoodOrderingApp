from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomeScreenView(TemplateView):
    template_name = "personal/home.html"
