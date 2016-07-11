# django
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
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
    print min(amount_czk, amount_btc)
    if min(filter(None, (amount_czk, amount_btc))) <= 0:
        return HttpResponseBadRequest('amount MUST BE POSITIVE')

    profile = get_object_or_404(Profile, token=token)

    tr = Transaction.create(
        profile=profile,
        amount_czk=amount_czk,
        amount_btc=amount_btc,
        description=description,
    )
    url = tr.url()

    if request.REQUEST.get('_redirect'):
        return HttpResponseRedirect(url)

    response = HttpResponse(url)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response


def payment_view(request, token):
    tr = get_object_or_404(Transaction, token=token)

    return render(request, 'transaction/payment.html', {
        'transaction': tr,
        'hide_menu': True,
    })


def creator_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    return render(request, 'transaction/creator.html', {
        'profile': profile,
        'ORIGIN': settings.ORIGIN,
    })
