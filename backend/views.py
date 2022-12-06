from django.shortcuts import render
from .models import Post, TopPost, LatestPost

def home(request):
    posts = Post.objects.all()
    tposts = TopPost.objects.all()
    lposts = LatestPost.objects.all()
    context = {
        "posts": posts,
        "tposts": tposts,
        "lposts": lposts
    }
    return render(request, "index.html", context)
