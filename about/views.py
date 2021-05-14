from django.shortcuts import render

# Create your views here.


def about(request):
    """ A view to return the custom order/print page """

    return render(request, 'about/about.html')
