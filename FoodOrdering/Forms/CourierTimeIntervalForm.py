from django.forms import ModelForm

from personal.models import CourierProfile


class CourierTimeIntervalForm(ModelForm):
    class Meta:
        model = CourierProfile
        exclude = ['divident ', 'phone_number', 'user']

    field_order = ['']
