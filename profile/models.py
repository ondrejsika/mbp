# django
from django.db import models

# app
from account.models import Account


class Profile(models.Model):
    account = models.ForeignKey(Account)
    wallet = models.CharField(max_length=40)
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __unicode__(self):
        return u'%s' % self.name

