from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    limit = request.GET.get('limit', '2')
    offset = request.GET.get('offset', '0')
    posts = models.Post.objects.all()[int(offset): int(limit) + int(offset)]
    about = models.AboutLogin.objects.filter(id=1)
    context = {
        'posts': posts,
        'about': about
    }
    return render(request, "index.html", context=context)
