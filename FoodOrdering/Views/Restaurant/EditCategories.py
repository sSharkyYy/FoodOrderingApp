from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import View

from FoodOrdering.Forms.CategoriesForm import CategoriesForm
from personal.models import Types


class EditCategories(PermissionRequiredMixin, LoginRequiredMixin, View):
    template = 'FoodOrdering/Restaurant/edit_categories.html'
    form = CategoriesForm

    def has_permission(self):
        return True

    def get_existing_profile(self):
        return Types.objects.filter(owner_id=self.request.user).first()

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
