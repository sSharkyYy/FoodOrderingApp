from django.core.exceptions import ValidationError

from django.forms import forms, EmailField, CharField, ChoiceField


class CreateOrderForm(forms.Form):
    shipping = ChoiceField(choices=((1, 'Házhozszállítás'), (2, 'Átvétel')))
    phone_number = CharField(max_length=10)
    address = CharField(required=False, max_length=254)
    name = CharField(required=True, max_length=254)

    def clean(self):
        results = super().clean()
        shipping = results.get('shipping', None)
        address = results.get('address', None)
        if shipping == 1 and address is None:
            raise ValidationError('Cím kitöltése kötelező házhozszállítás esetén')
        return results
