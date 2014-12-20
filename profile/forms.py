# django
from django import forms

# local
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('account', )

    def __init__(self, account, *args, **kwargs):
        self.account = account
        super(ProfileForm, self).__init__(*args, **kwargs)

        if not account.priv_editable_xpubs and kwargs['instance']:
            del self.fields['xpub']

    def save(self, commit=True):
        obj = super(ProfileForm, self).save(commit=False)
        obj.account = self.account
        if commit == True:
            obj.save()
        return obj
