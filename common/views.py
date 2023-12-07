from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    posts = models.Post.objects.all()[:2]
    about = models.AboutLogin.objects.filter(id=1)
    context = {
        'posts': posts,
        'about': about
    }
    return render(request, "index.html", context=context)
