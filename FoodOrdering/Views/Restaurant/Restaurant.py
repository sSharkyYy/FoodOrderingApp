from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView


class CreateRestaurant(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    def has_permission(self):
        return True

    template_name = 'offers/offer_detail.html'

    def get_context_data(self, **kwargs):
        """ Adds extra content to our template """
        context = super().get_context_data(**kwargs)
        context['address_form'] = 1
        context['restaurant_form'] = 1
        return context

    ### NegotiationGroupDetailView
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if context['address_form'].is_valid():
            instance = context['negotiation_bid_form'].save()
            messages.success(request, 'Your offer bid #{0} has been submitted.'.format(instance.pk))
        elif context['restaurant_form'].is_valid():
            instance = context['offer_attachment_form'].save()
            messages.success(request, 'Your offer attachment #{0} has been submitted.'.format(instance.pk))
            # advise of any errors

        else:
            messages.error('Error(s) encountered during form processing, please review below and re-submit')

        return self.render_to_response(context)
