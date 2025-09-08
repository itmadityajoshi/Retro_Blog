from django.shortcuts import render
from .models import Category

# Create your views here.
def post(req):
    categories= Category.objects.all()
    context = {
        'categories': categories
    }
    return render(req, 'post.html', context)


def worldPost(req):
    return render(req, 'world.html')