from django.shortcuts import render

from worldOfSpeed.profiles.models import Profile


def index(request):
    profile = Profile.objects.first()

    context = {
        "profile": profile
    }

    return render(
        request,
        'home/index.html',
        context
    )
