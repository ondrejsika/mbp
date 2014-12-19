# django
from django.db import models

# django contrib
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField()
    token = models.CharField(max_length=32)

    def __unicode__(self):
        return u'%s' % self.user