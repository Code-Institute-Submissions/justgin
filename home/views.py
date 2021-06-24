from django.shortcuts import render


def index(request):
    """ Index View """
    return render(request, 'home/index.html')


def about(request):
    """ About Page View """
    return render(request, 'home/about.html')
