from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def userLogin(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')

    context = {}
    return render(request, 'users/login_register.html', context)


def userLogout(request):
    logout(request)
    return redirect('profiles')


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
