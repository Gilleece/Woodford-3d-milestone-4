from django.shortcuts import render

# Create your views here.


def custom_print(request):
    """ A view to return the custom order/print page """

    return render(request, 'custom_order/custom_order.html')
