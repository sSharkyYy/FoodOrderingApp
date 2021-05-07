from builtins import staticmethod

from django.db.models import Sum
from django.utils import timezone

from personal.models import Payments


class CourierService:

    @staticmethod
    def get_payments(courier_profile):
        return Payments.objects.values('date__month').filter(
            courier=courier_profile).annotate(total_money=Sum('money'))

    @staticmethod
    def get_monthly_payment(courier_profile, date=None):
        if date is None:
            date = timezone.now()
        return CourierService.get_payments(courier_profile).filter(date__month=date.month).first()
