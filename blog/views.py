from django.shortcuts import render, get_object_or_404

from .models import Post


def all_posts(request):
    """ A view to return the main blog page """

    blogs = Post.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/all_posts.html', context)

    
def blog_post(request, url):
    """ A view to return the main blog page """

    blog = get_object_or_404(Post, url=url)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_post.html', context)
