from django.forms import ModelForm

from personal.models import Types


class AddCategoriesForm(ModelForm):
    class Meta:
        model = Types
        exclude = ['owner']
