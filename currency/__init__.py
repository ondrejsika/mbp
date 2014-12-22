# local
from .models import Currency, ProfileCurrency


def to_btc_czk(amount_btc=None, amount_czk=None, profile=None):
    assert None != amount_btc or None != amount_czk

    # FIXME: temporaily - use decimals
    amount_btc = float(amount_btc) if amount_btc else None
    amount_czk = float(amount_czk) if amount_czk else None

    czk_rate = Currency.objects.get(name=Currency.CZK).rate
    if profile:
        try:
            czk_rate = ProfileCurrency.objects.get(name=ProfileCurrency.CZK, profile=profile).rate
        except ProfileCurrency.DoesNotExist:
            pass

    if amount_btc:
        amount_czk = amount_btc * czk_rate
    elif amount_czk:
        amount_btc = amount_czk / czk_rate

    return amount_btc, amount_czk, czk_rate