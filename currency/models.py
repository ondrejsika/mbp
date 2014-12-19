# django
from django.db import models


class Currency(models.Model):
    CZK = 'CZK'

    CURRENCIES = {
        CZK: 'CZK',
    }
    name = models.CharField(max_length=3, choices=CURRENCIES.items(), unique=True)
    rate = models.FloatField()

    def __unicode__(self):
        return u'%s %s' % (self.name, self.rate)