from django.forms import forms, EmailField, CharField, ChoiceField


class CreateOrderForm(forms.Form):
    shipping = ChoiceField(choices=((1, 'Házhozszállítás'), (2, 'Átvétel')))
    phone_number = CharField(max_length=10)
    address = CharField(required=True, max_length=254)
    name = CharField(required=True, max_length=254)

