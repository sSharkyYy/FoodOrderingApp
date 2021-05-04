from django.urls import reverse
from django.views.generic import UpdateView

from personal.models import Order


class UpdateOrders(UpdateView):
    model = Order
    template_name = 'FoodOrdering/Courier/Orders/order_update_form.html'

    fields = ['status']

    def get_success_url(self):
        return reverse('FoodOrdering:list_orders')
