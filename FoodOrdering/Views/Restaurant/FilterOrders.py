from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from django.db.models import Sum

from FoodOrdering.Forms.FilterOrdersForm import FilterOrdersForm
from FoodOrdering.services.ProfileService import ProfileService
from personal.models import Order, Payments


class FilterOrders(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    def has_permission(self):
        try:
            self.restaurant = ProfileService.get_restaurant_profile(self.request.user)
            return True
        except ValueError:
            pass
        return False

    model = Order
    template_name = 'FoodOrdering/Restaurant/filter_orders.html'
    form = FilterOrdersForm

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(FilterOrders, self).get_context_data()
        form = self.create_form()
        payments = Payments.objects.filter(order__cart__restaurant=self.restaurant)

        if form.is_valid():
            from_date = form.cleaned_data.get('from_date')
            to_date = form.cleaned_data.get('to_date')
            payments = payments.filter(date__range=[from_date, to_date])

        context['payment'] = payments.aggregate(Sum('money'))
        context['form'] = form
        return context

    def create_form(self):
        form = self.form()
        if self.request.GET.get('from_date', None) is not None:
            form = self.form(self.request.GET)
        return form

    def get_queryset(self):
        qs = super(FilterOrders, self).get_queryset()
        form = self.create_form()
        if form.is_valid():
            from_date = form.cleaned_data.get('from_date')
            to_date = form.cleaned_data.get('to_date')
            qs = qs.filter(order_date__range=[from_date, to_date])
        qs = qs.filter(cart__restaurant=self.restaurant)
        return qs
