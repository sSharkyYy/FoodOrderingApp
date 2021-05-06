from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import ListView

from FoodOrdering.services.DishService import DishService
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Order,OrderStatus


class ListPayments(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'FoodOrdering/Courier/list_payments.html'
    context_object_name = 'orders'
    ordering = ['order_date']

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(status=OrderStatus.Ordered.value)

        return qs
