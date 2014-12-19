# django
from django.db import models

# app
from profile.models import Profile


class Transaction(models.Model):
    UNCONFIRMED = 'u'
    CONFIRMED = 'c'
    STATES = {
        CONFIRMED: 'Confirmed',
        UNCONFIRMED: 'Unconfirmed',
    }

    profile = models.ForeignKey(Profile)
    amount_btc = models.DecimalField(max_digits=9, decimal_places=8)
    amount_czk = models.DecimalField(max_digits=9, decimal_places=2)
    state = models.CharField(max_length=1, choices=STATES.items())
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'#%s %s BTC %s CZK' % (self.id, self.amount_btc, self.amount_czk)