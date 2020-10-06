from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('acerca-de/', v.about, name='about'),
    path('en-adopción/', v.adopt, name='adopt'),
    path('blog/', v.blog, name='blog'),
    path('donaciones/', v.donate, name='donate'),

]
