from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomeScreenView(TemplateView):
    template_name = "personal/home.html"
    extra_context = {}

    first = {}
    second = {}
    first['rest_id'] = 1
    first['rest_name'] = "Étterem 1"
    first['rest_address'] = "Cim"
    first['rest_text'] = "bla bla bla"
    second['rest_id'] = 2
    second['rest_name'] = "Étterem 2"
    second['rest_address'] = "Cim"
    second['rest_text'] = "bla bla bla"

    list_of_values = []
    list_of_values.append(first)
    list_of_values.append(second)

    extra_context['list_of_values'] = list_of_values
