from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Blog
from core.models import PaginaBlog

class BlogListView(ListView):

    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blog_list"
    queryset = Blog.objects.order_by('-id').filter(published=True)
    paginate_by = 3

    def get_context_data(self, **kwargs):
        queries = super(BlogListView, self).get_context_data(**kwargs)
        queries['seo_description'] = PaginaBlog.objects.get(id=1).seo_description
        return queries

class BlogDetailView(DetailView):

    model = Blog
    template_name = "blog/blog_detail.html"
