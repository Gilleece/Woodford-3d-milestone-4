from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Product
from .forms import ProductForm


def all_products(request):
    """ A view to return the products page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'product/products.html', context)


def product_detail(request, product_id):
    """ A view to return the page for a specific product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'product/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)