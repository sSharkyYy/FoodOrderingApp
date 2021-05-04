from django.forms import forms, DateTimeField


class FilterOrdersForm(forms.Form):
    from_date = DateTimeField(required=True, help_text='YYYY-MM-DD')
    to_date = DateTimeField(required=True, help_text='YYYY-MM-DD')
