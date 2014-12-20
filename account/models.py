# django
from django.db import models
from django.db.models.signals import post_save

# django contrib
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()

    # privileges
    priv_editable_xpubs = models.BooleanField(default=False)
    priv_can_create_profile = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.user

    def get_confirmed_amount(self):
        from transaction.models import Transaction

        return Transaction.objects.filter(profile__account=self, state=Transaction.CONFIRMED)\
            .aggregate(btc=models.Sum('amount_btc'),
                       czk=models.Sum('amount_czk'))

    def get_unconfirmed_amount(self):
        from transaction.models import Transaction

        return Transaction.objects.filter(profile__account=self, state=Transaction.UNCONFIRMED) \
            .aggregate(btc=models.Sum('amount_btc'),
                       czk=models.Sum('amount_czk'))

    def save(self, update_user=True, **kwargs):
        if update_user:
            self.user.email = self.email
            self.user.save()
        super(Account, self).save(**kwargs)


def user_post_save(sender, instance, created, **kwargs):
    if not hasattr(instance, 'account'):
        instance.account = Account(user=instance, email=instance.email)
    instance.account.email = instance.email
    instance.account.save(update_user=False)


post_save.connect(user_post_save, sender=User)