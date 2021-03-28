from django.contrib import admin

from Auth import models
from .models import Profile

# Register your models here.
admin.site.register(models.User)
admin.site.register(Profile)
