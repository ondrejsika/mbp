# django
from django.shortcuts import render

# django contrib
from django.contrib.auth.decorators import login_required

# project
from transaction.models import Transaction
from main_utils.paginator import get_page_from_request


@login_required
def dashboard_view(request):
    all_transactions = Transaction.objects.filter(profile__account=request.user.account)
    all_transactions = get_page_from_request(all_transactions, request)

    return render(request, 'account/dashboard.html', {
        'all_transactions': all_transactions,
    })