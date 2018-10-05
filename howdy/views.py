from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Post
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic import ListView

# Create your views here.
class HomePageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"
    def get(self, request, **kwargs):
        postItem = Post.objects.get(postNum=2)
        #template = loader.get_template('/about.html')
        context = {
            'postItem' : postItem,
        }
        return render(request,"about.html",context)

class AboutList(ListView):
    model = Post
