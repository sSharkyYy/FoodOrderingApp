from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View

from personal.models import Order, OrderStatus


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

        if reject and reject == '1':
            order.courier = None

        if delivered and delivered == '1':
            order.status = OrderStatus.Delivered.value

        order.save()

        return redirect('FoodOrdering:list_orders')
