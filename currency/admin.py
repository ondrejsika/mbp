# django contrib
from django.contrib import admin

# local
from .models import Currency, ProfileCurrency


admin.site.register(Currency)
admin.site.register(ProfileCurrency)
