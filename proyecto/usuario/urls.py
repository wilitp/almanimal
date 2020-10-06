from django.urls import path
from . import views

urlpatterns = [
    
    path('iniciar-sesion/', views.logIn, name="iniciar-sesion"),
    path('cerrar-sesion/', views.logOut, name="cerrar-sesion"),
    path('registro/', views.registro, name="registro"),

]