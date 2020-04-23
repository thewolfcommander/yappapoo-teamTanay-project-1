from django.shortcuts import render

from products.models import Seller, Category, Product


def home(request):
    """
    Home page for the entire application
    """
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'core/home.html', context)