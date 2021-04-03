from django.views.generic import DeleteView

from personal.models import Types


class DeleteType(DeleteView):
    model = Types
    success_url = '/'
    template_name = 'FoodOrdering/Restaurant/Types/confirm_delete_types.html'
