# django
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponseForbidden

# django contrib
from django.contrib.auth.decorators import login_required

# local
from .models import Profile
from .forms import ProfileForm


@login_required
def detail_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    return render(request, 'profile/detail.html', {
        'profile': profile,
    })


@login_required
def edit_view(request, profile_id=None):
    if profile_id:
        profile = get_object_or_404(Profile, id=profile_id, account=request.user.account)
    else:
        if not request.user.account.priv_can_create_profile:
            return HttpResponseForbidden('403 Forbidden')
        profile = None

    form = ProfileForm(request.user.account, request.POST or None, instance=profile)
    if form.is_valid():
        profile = form.save()
        return HttpResponseRedirect(reverse('profile:detail', args=(profile.id,)))

    return render(request, 'profile/edit.html', {
        'profile': profile,
        'form': form,
    })
