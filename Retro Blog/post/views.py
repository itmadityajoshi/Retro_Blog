from django.shortcuts import render

# Create your views here.
def post(req):
    return render(req, 'post.html')


def worldPost(req):
    return render(req, 'world.html')