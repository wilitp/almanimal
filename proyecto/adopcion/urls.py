"""adopcion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import AdopcionListView, AdopcionDetailView, AdopcionFormView, AdopcionUpdateView, AdopcionDeleteView

urlpatterns = [
    
    path('adopcion/', AdopcionListView.as_view(), name='adopcion'),
    path('adopcion/<int:pk>', AdopcionDetailView.as_view(), name='adopcion-detail'),
    path('adopcion/agregar-animal', AdopcionFormView.as_view(), name='agregar-animal'),
    path('adopcion/editar-animal/<int:pk>', AdopcionUpdateView.as_view(), name='editar-animal'),
    path('adopcion/eliminar-animal/<int:pk>', AdopcionDeleteView.as_view(), name='eliminar-animal'),

]