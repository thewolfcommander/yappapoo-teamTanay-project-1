from django.shortcuts import render


def home(request):
    """
    Home page for the entire application
    """
    context = {}
    return render(request, 'core/home.html', context)