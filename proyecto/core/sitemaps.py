from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.urls import reverse

from blog.models import Blog

class StaticSitemap(Sitemap):

    changefreq = "daily"
    priority = 0.5
    protocol = "https"

    def get_urls(self, site=None, **kwargs):
        site = Site(domain="fundacionalmanimalmendiolaza.com.ar", name="fundacionalmanimalmendiolaza.com.ar")
        return super(StaticSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['home', 'adopcion', 'donaciones', 'contacto', 'blog']

    def location(self, item):
        return reverse(item)


class DynamicSitemap(Sitemap):

    changefreq = "daily"
    priority = 0.5
    protocol = "https"

    def get_urls(self, site=None, **kwargs):
        site = Site(domain="fundacionalmanimalmendiolaza.com.ar", name="fundacionalmanimalmendiolaza.com.ar")
        return super(DynamicSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return Blog.objects.all().filter(published=True).order_by('-id')

    def lastmod(self, obj):
        return obj.last_updated

    def location(self, item):
        return "/blog/detail/" + str(item)