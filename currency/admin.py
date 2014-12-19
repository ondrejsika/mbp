# django contrib
from django.contrib import admin

# local
from .models import Currency


admin.site.register(Currency)
