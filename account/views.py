# django
from django.shortcuts import render

# django contrib
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_view(request):
    return render(request, 'account/dashboard.html', {})