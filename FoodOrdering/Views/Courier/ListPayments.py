from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from FoodOrdering.services.CourierService import CourierService
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Payments


class ListPayments(LoginRequiredMixin, View):
    model = Payments
    template_name = 'FoodOrdering/Courier/list_payments.html'
    context_object_name = 'payments'

    def get(self, request, *args, **kwargs):
        payments = CourierService.get_payments(ProfileService.get_courier_profile(request.user))
        return render(request, self.template_name, {'payments': payments})

    # ordering = ['order_date']
