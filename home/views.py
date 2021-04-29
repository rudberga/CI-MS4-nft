from django.shortcuts import render


def index(request):
    """ View to return index page """

    return render(request, 'home/index.html')


def about(request):
    """ View to go to about page """

    return render(request, 'home/about.html')