from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):

    changefreq = "daily"
    priority = 0.5

    def items(self):
        return ['home', 'adopcion', 'donaciones', 'contacto', 'blog']

    def location(self, item):
        return reverse(item)