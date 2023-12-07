from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    offset = request.GET.get('offset', '0')
    posts = models.Post.objects.all()
    context = {
        'posts': posts[int(offset):2 + int(offset)],
        'about': models.AboutLogin.objects.all().first(),
        'last': int(offset) - 2,
        'next': int(offset) + 2,
        'is_last': not int(offset) == 0,
        'is_next': not 2 + int(offset) >= posts.count()
    }
    return render(request, "index.html", context=context)
