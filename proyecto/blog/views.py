from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Blog

class BlogListView(ListView):

    context_object_name = 'blog_list'
    queryset = Blog.objects.order_by('-id').filter(published=True)
    template_name = "blog/blog_list.html"

class BlogDetailView(DetailView):

    model = Blog
    template_name = "blog/blog_detail.html"
