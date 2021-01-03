from django.urls import path
from . import views

urlpatterns = [
    
    path('blog', views.BlogListView.as_view(), name='blog'),
    path('blog/detail/<pk>/<title>', views.BlogDetailView.as_view(), name='blog_detail'),

]
