from django.shortcuts import render
from .models import Post, TopPost, LatestPost
from django.views.generic import TemplateView

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


class AboutView(TemplateView):
    template_name = "about.html"

class AuthorView(TemplateView):
    template_name = "author.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class FullleftView(TemplateView):
    template_name = "index-full-left.html"

class FullrightView(TemplateView):
    template_name = "index-full-right.html"

class FullView(TemplateView):
    template_name = "index-full.html"

class ListrightView(TemplateView):
    template_name = "index-list-right.html"

class ListleftView(TemplateView):
    template_name = "index-list-left.html"

class ListView(TemplateView):
    template_name = "index-list.html"

class Postd1View(TemplateView):
    template_name = "post-details-1.html"

class Postd2View(TemplateView):
    template_name = "post-details-2.html"

class PostelementsView(TemplateView):
    template_name = "post-elements.html"

class PrivacyView(TemplateView):
    template_name = "privacy-policy.html"

class TermsView(TemplateView):
    template_name = "terms-conditions.html"