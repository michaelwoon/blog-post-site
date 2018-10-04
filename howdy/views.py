from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Post
from django.http import HttpResponse

# Create your views here.
def getData(request):
    postItem = Post.objects.get(author="Thomas Jefferson")
    #template = loader.get_template('/about.html')
    context = {
        'postItem' : postItem
    }
    return render("about.html",context)

class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"
