from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    offset = request.GET.get('offset', '0')
    posts = models.Post.objects.all()
    count = posts.count()
    is_last = not int(offset) == 0
    is_next = not 2 + int(offset) >= count
    about = models.AboutLogin.objects.all().first()
    context = {
        'posts': posts[int(offset):2 + int(offset)],
        'about': about,
        'last': int(offset) - 2,
        'next': int(offset) + 2,
        'is_last': is_last,
        'is_next': is_next
    }
    return render(request, "index.html", context=context)
