from django.shortcuts import render
from .models import Category, Blog

# Create your views here.
def post(req):
    categories= Category.objects.all()
    featured_post = Blog.objects.all()
    context = {
        'categories': categories,
        'featured_post' : featured_post
    }
    return render(req, 'post.html', context)


def worldPost(req):
    return render(req, 'world.html')