from django.views.generic import UpdateView

from personal.models import Types


class UpdateType(UpdateView):
    model = Types
    template_name = 'FoodOrdering/Restaurant/Types/type_update_form.html'

    fields = ['name']
