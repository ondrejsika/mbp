# django
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.conf import settings

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

    if not bool(amount_czk) != bool(amount_btc):
        return HttpResponseBadRequest('amount_czk XOR amount_btc')

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


def creator_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    return render(request, 'transaction/creator.html', {
        'profile': profile,
        'ORIGIN': settings.ORIGIN,
    })
