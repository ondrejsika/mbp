# django
from django.db import models
from django.db.models.signals import post_save

# django contrib
from django.contrib.auth.models import User

# app
from main_utils import timestamp_random_string


class Account(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    token = models.CharField(max_length=32, unique=True, default=timestamp_random_string)

    def __unicode__(self):
        return u'%s' % self.user

    def save(self, update_user=True, **kwargs):
        if update_user:
            self.user.email = self.email
            self.user.save()
        super(Account, self).save(**kwargs)


def user_post_save(sender, instance, created, **kwargs):
    if not instance.account:
        instance.account = Account(user=instance, email=instance.email)
    instance.account.email = instance.email
    instance.account.save(update_user=False)


post_save.connect(user_post_save, sender=User)