from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Blog

class StaticSitemap(Sitemap):

    changefreq = "daily"
    priority = 0.5

    def items(self):
        return ['home', 'adopcion', 'donaciones', 'contacto', 'blog']

    def location(self, item):
        return reverse(item)


class DynamicSitemap(Sitemap):

    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Blog.objects.all().filter(published=True).order_by('-id')

    def lastmod(self, obj):
        return obj.last_updated

    def location(self, item):
        return "/blog/detail/" + str(item)