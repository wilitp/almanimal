from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime
from django.contrib import messages
from smtplib import SMTPException
from .models import ContactForm
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contact.html', {'form': ContactForm})

def donaciones(request):
    return render(request, 'core/donaciones.html')
