# django
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# app
from profile.models import Profile

# local
from .models import Transaction


def create_view(request):
    token = request.REQUEST.get('token')
    description = request.REQUEST.get('description', '')
    try:
        amount_btc = request.REQUEST.get('amount_btc')
        float(amount_btc)
    except (ValueError, TypeError):
        amount_btc = None
    try:
        amount_czk = request.REQUEST.get('amount_czk')
        float(amount_czk)
    except (ValueError, TypeError):
        amount_czk = None

    profile = get_object_or_404(Profile, token=token)

    tr = Transaction.create(
        profile=profile,
        amount_czk=amount_czk,
        amount_btc=amount_btc,
        description=description,
    )
    return HttpResponse(tr.url())


def payment_view(request, token):
    tr = get_object_or_404(Transaction, token=token)

    return render(request, 'transaction/payment.html', {
        'transaction': tr,
    })