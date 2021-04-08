from django.forms import forms, EmailField, CharField


class CreateOrderForm(forms.Form):
    address = CharField(required=True, max_length=254)
    name = CharField(required=True, max_length=254)
