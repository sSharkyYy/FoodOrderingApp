from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import View

from FoodOrdering.Forms.CourierTimeIntervalForm import CourierTimeIntervalForm
from personal.models import CourierProfile


class EditCourierTimeInt(PermissionRequiredMixin, LoginRequiredMixin, View):
    template = 'FoodOrdering/Courier/edit.html'
    form = CourierTimeIntervalForm

    def has_permission(self):
        return True

    def get_existing_profile(self):
        return CourierProfile.objects.filter(user=self.request.user).first()

    def get(self, request, *args, **kwargs):
        form = self.form(instance=self.get_existing_profile())
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        existing_profile = self.get_existing_profile()
        form = self.form(request.POST, instance=existing_profile)
        if form.is_valid():
            obj = form.save(commit=False)
            if existing_profile is None:
                obj.user = self.request.user
            obj.save()
            messages.success(request, 'Profile Save')
            return redirect('/')
        return render(request, self.template, {'form': form})
