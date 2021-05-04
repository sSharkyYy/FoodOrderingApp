from django.forms import forms, EmailField, CharField, ChoiceField


class CreateOrderForm(forms.Form):
    address = CharField(required=True, max_length=254)
    name = CharField(required=True, max_length=254)
    shipping = ChoiceField(choices=((1, 'Házhozszállítás'), (2, 'Átvétel')))
