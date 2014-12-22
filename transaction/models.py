# django
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# app
from profile.models import Profile
from currency import to_btc_czk
from main_utils import timestamp_random_string
from main_utils.wallet import get_wallet_from_xpub
from main_utils.qrcode_utils import qrcode_datauri

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
    token = models.CharField(max_length=32, unique=True, default=timestamp_random_string, db_index=True)
    amount_btc = models.DecimalField(max_digits=12, decimal_places=8)
    amount_czk = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.CharField(max_length=1, choices=STATES.items(), default=UNCONFIRMED)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, default='')

    wallet = models.CharField(max_length=40)

    class Meta:
        ordering = ('-pk', )

    def __unicode__(self):
        return u'#%s %s BTC %s CZK' % (self.id, self.amount_btc, self.amount_czk)

    def save(self, *args, **kwargs):
        ret = super(Transaction, self).save(*args, **kwargs)
        if not self.wallet:
            self.wallet = get_wallet_from_xpub(self.profile.xpub, self.id)
        return ret

    @staticmethod
    def create(profile, amount_btc=None, amount_czk=None, description=''):
        amount_btc, amount_czk = to_btc_czk(amount_btc, amount_czk)
        tr = Transaction(
            profile=profile,
            amount_btc=amount_btc,
            amount_czk=amount_czk,
            description=description,
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
        return settings.ORIGIN + reverse('tr:payment_detail', args=(self.token, ))

    def get_payment_qrcode(self):
        return qrcode_datauri('bitcoin:%s?amount=%s' % (self.wallet, self.amount_btc))
