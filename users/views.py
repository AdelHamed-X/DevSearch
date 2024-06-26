from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm

# Create your views here.

def userLogin(request):
    page = 'login'
    if request.user.is_authenticated:
        messages.add_message(request, messages.SUCCESS, "You're already signed in!")
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Signed in successfully!")
            return redirect('profiles')
        else:
            messages.add_message(request, messages.SUCCESS, "Invalid Username or Password!")

    context = {'page': page}
    return render(request, 'users/login_register.html', context)


def userRegister(request):
    page = 'register'

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Account Created Successfully!')

            return redirect('login')
        else:
            messages.error(request, 'An error occurred during registration!')
    else:
        form = UserRegistrationForm()


    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def userLogout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logged out successfully!")
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
