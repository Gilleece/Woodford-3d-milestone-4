from django.shortcuts import render


def all_posts(request):
    """ A view to return the main blog page """
    return render(request, 'blog/all_posts.html')
