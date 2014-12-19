# django contrib
from django.contrib import admin

# local
from .models import Account


admin.site.register(Account)
