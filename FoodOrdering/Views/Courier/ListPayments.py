from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import ListView

from FoodOrdering.services.DishService import DishService
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Payments


class ListPayments(LoginRequiredMixin, ListView):
    model = Payments
    template_name = 'FoodOrdering/Courier/list_payments.html'
    context_object_name = 'payments'


    # ordering = ['order_date']


