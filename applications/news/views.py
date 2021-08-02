from django.views.generic import View, DetailView
from django.shortcuts import render
from .models import Post
# Create your views here.

class MainPage(View):

    def get(self, request):
        post = Post.objects.filter(is_active=True )
        return render(request, 'main_page.html', context={'post': post})


class NewsDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news_detail.html'
    