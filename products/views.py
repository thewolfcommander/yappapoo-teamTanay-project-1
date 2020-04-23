from django.shortcuts import render, get_object_or_404

from .models import *

def product_detail(request, pk=None, *args, **kwargs):
    """
    View for detail of single product
    """
    product = get_object_or_404(Product, id=pk)
    # others = Products.objects.filter