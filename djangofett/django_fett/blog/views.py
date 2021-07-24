from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# fake posts for demo purposes, something one might get from say aa database
posts = [
    {
        'author': "Trevor Viken",
        'title': "Blog Post 1",
        'content': 'First Post Content',
        'date_posted': 'August 27, 2021'
    },
    {
        'author': "Addison Woll",
        'title': "Blog Post 2",
        'content': 'First Post Content',
        'date_posted': 'August 28, 2021'
    }
]


def home(request) -> HttpResponse:
    context = {
        #'posts': posts
        'posts': Post.objects.all(),

    }
    return render(request=request,
                  template_name='blog/home.html',
                  context=context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request=request,
                  template_name='blog/about.html',
                  context=context)
