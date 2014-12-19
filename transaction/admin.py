# django contrib
from django.contrib import admin

# local
from .models import Transaction


admin.site.register(Transaction)
