# django
from django import forms
from django.conf import settings

# local
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('account', 'token', )

    def __init__(self, account, *args, **kwargs):
        self.account = account
        self.instance = kwargs['instance']
        super(ProfileForm, self).__init__(*args, **kwargs)

        if not account.priv_editable_xpubs:
            del self.fields['xpub']

    def save(self, commit=True):
        obj = super(ProfileForm, self).save(commit=False)
        obj.account = self.account
        if not obj.xpub:
            obj.xpub = settings.DEFAULT_XPUB
        if commit == True:
            obj.save()
        return obj
