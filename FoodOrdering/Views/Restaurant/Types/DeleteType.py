from django.urls import reverse
from django.views.generic import DeleteView

from personal.models import Types


class DeleteType(DeleteView):
    model = Types
    template_name = 'FoodOrdering/Restaurant/Types/confirm_delete_types.html'

    def get_success_url(self):
        return reverse('FoodOrdering:list_types')
