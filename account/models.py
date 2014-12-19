# django
from django.db import models

# django contrib
from django.contrib.auth.models import User

# app
from main_utils import timestamp_random_string


class Account(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField()
    token = models.CharField(max_length=32, unique=True, default=timestamp_random_string)

    def __unicode__(self):
        return u'%s' % self.user