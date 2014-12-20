# django
from django.db import models

# app
from account.models import Account


class Profile(models.Model):
    account = models.ForeignKey(Account)
    name = models.CharField(max_length=64)
    description = models.TextField()
    xpub = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % self.name

    def get_confirmed_amount(self):
        from transaction.models import Transaction

        return self.transaction_set.filter(state=Transaction.CONFIRMED).aggregate(btc=models.Sum('amount_btc'),
                                                                                  czk=models.Sum('amount_czk'))

    def get_unconfirmed_amount(self):
        from transaction.models import Transaction

        return self.transaction_set.filter(state=Transaction.UNCONFIRMED).aggregate(btc=models.Sum('amount_btc'),
                                                                                    czk=models.Sum('amount_czk'))
