from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View
from FoodOrdering.services.ProfileService import ProfileService

from personal.models import Order, OrderStatus, Payments


class UpdateOrders(View):
    model = Order

    def post(self, request, *args, **kwargs):
        id = request.POST.get('order', None)
        accept = request.POST.get('accept', None)
        reject = request.POST.get('reject', None)
        delivered = request.POST.get('delivered', None)
        order = get_object_or_404(self.model, pk=id)

        if accept and accept == '1':
            order.status = OrderStatus.UnderDelivery.value
            entry = Order.objects.get(pk=id)

        if reject and reject == '1':
            order.courier = None
            order.status = OrderStatus.Ordered.value

        if delivered and delivered == '1':
            order.status = OrderStatus.Delivered.value
            amount = Order.objects.get(pk=id).amount
            P = Payments(money=amount, courier=ProfileService.get_courier_profile(self.request.user), order=order)
            P.save()

        order.save()

        return redirect('FoodOrdering:list_orders')
