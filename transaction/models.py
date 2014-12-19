# django
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# app
from profile.models import Profile
from currency import to_btc_czk
from main_utils import timestamp_random_string
from main_utils.wallet import get_wallet_from_xpub

# local
from .utils import is_confirmed


class Transaction(models.Model):
    UNCONFIRMED = 'u'
    CONFIRMED = 'c'
    STATES = {
        CONFIRMED: 'Confirmed',
        UNCONFIRMED: 'Unconfirmed',
    }

    profile = models.ForeignKey(Profile)
    token = models.CharField(max_length=32, unique=True, default=timestamp_random_string)
    amount_btc = models.DecimalField(max_digits=9, decimal_places=8)
    amount_czk = models.DecimalField(max_digits=9, decimal_places=2)
    state = models.CharField(max_length=1, choices=STATES.items(), default=UNCONFIRMED)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def wallet(self):
        return get_wallet_from_xpub(self.profile.xpub, self.id)

    def __unicode__(self):
        return u'#%s %s BTC %s CZK' % (self.id, self.amount_btc, self.amount_czk)

    @staticmethod
    def create(profile, amount_btc=None, amount_czk=None):
        amount_btc, amount_czk = to_btc_czk(amount_btc, amount_czk)
        tr = Transaction(
            profile=profile,
            amount_btc=amount_btc,
            amount_czk=amount_czk,
        )
        tr.save()
        return tr

    @staticmethod
    def confirm_transactions():
        for tr in Transaction.objects.filter(state=Transaction.UNCONFIRMED):
            if is_confirmed(tr):
                tr.state = Transaction.CONFIRMED
                tr.save()


    def url(self):
        return settings.ORIGIN + reverse('tr:detail', args=(self.token, ))