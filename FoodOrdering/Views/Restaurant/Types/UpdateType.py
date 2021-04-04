from django.urls import reverse
from django.views.generic import UpdateView

from personal.models import Types


class UpdateType(UpdateView):
    model = Types
    template_name = 'FoodOrdering/Restaurant/Types/type_update_form.html'

    fields = ['name']

    def get_success_url(self):
        return reverse('FoodOrdering:list_types')
