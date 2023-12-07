from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    offset = request.GET.get('offset', '0')
    posts = models.Post.objects.all()
    count = posts.count()
    about = models.AboutLogin.objects.filter(id=1)
    context = {
        'posts': posts[int(offset):2 + int(offset)],
        'about': about,
        'last': int(offset) - 2,
        'next': int(offset) + 2
    }
    return render(request, "index.html", context=context)
