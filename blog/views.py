from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import BlogForm


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


@login_required
def add_post(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('add_post'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = BlogForm()
        
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, url):
    """ Edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Post, url=url)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('blog_post', args=[url]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing the post: {blog.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_post(request, url):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Post, url=url)
    blog.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
