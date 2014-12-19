# django contrib
from django.contrib import admin

# local
from .models import Profile


admin.site.register(Profile)