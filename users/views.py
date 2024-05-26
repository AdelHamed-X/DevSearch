from django.shortcuts import render

# Create your views here.


def profiles(request):
    """ main profiles page """
    context = {}
    return render(request, 'users/profiles.html', context)
