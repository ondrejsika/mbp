# django
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# django contrib
from django.contrib.auth.decorators import login_required

# local
from .models import Profile


@login_required
def detail_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    return render(request, 'profile/detail.html', {
        'profile': profile,
    })