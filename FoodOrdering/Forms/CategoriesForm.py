from django.forms import ModelForm

from personal.models import Types


class CategoriesForm(ModelForm):
    class Meta:
        model = Types
        exclude = ['owner']

    field_order = ['name']
