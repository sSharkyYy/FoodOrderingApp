from django.core.exceptions import ValidationError
from django.views.generic import CreateView

from FoodOrdering.Forms.AddCategories import AddCategoriesForm
from FoodOrdering.services.TypeService import TypeService
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Types


class AddType(CreateView):
    model = Types
    template_name = 'FoodOrdering/Restaurant/Types/Add.html'
    form_class = AddCategoriesForm

    def form_valid(self, form):
        self.object: Types = form.save(commit=False)
        self.object.type: Types = TypeService.get_restaurant_profile(self.request.user)


        return super().form_valid(form)

    def get_success_url(self):
        return '/'
