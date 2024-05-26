from django.shortcuts import render
from .models import Profile

# Create your views here.


def profiles(request):
    """ main profiles page """
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles,
    }
    return render(request, 'users/profiles.html', context)


def profile(request, pk):
    """ User profile page """
    profile = Profile.objects.get(id=pk)
    context = {
        'profile': profile,
    }
    return render(request, 'users/user-account.html', context)