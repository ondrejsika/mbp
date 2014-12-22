# django
from django.db import models

# app
from profile.models import Profile


class Currency(models.Model):
    CZK = 'CZK'

    CURRENCIES = {
        CZK: 'CZK',
    }

    name = models.CharField(max_length=3, choices=CURRENCIES.items(), unique=True)
    rate = models.FloatField()

    def __unicode__(self):
        return u'%s %s' % (self.name, self.rate)


class ProfileCurrency(models.Model):
    CZK = 'CZK'

    CURRENCIES = {
        CZK: 'CZK',
    }

    name = models.CharField(max_length=3, choices=CURRENCIES.items())
    rate = models.FloatField()
    profile = models.ForeignKey(Profile)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.rate)

    class Meta:
        unique_together = (('name', 'rate'), )