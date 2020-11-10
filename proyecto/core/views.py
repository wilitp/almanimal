from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime
from django.contrib import messages
from smtplib import SMTPException
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def contacto(request):

    if request.method == 'POST':

        nombre = request.POST.get('first_name')
        apellido = request.POST.get('last_name')
        email = request.POST.get('email')
        telefono = request.POST.get('tel')
        categoria = request.POST.get('contact_category')
        asunto = request.POST.get('subject')
        consulta = request.POST.get('body')

        if nombre == "" or apellido == "" or email == "" or asunto == "" or consulta == "" or categoria == "":
            return HttpResponse("Completá los campos obligatorios")

        fecha = str(datetime.now())

        context = ({'nombre': nombre, 'apellido': apellido, 'email': email, 'telefono': telefono, 'consulta': consulta, 'fecha': fecha, 'categoria': categoria})

        subject, from_email, to = str(asunto), str(email), 'almanimalmendiolaza@gmail.com'
        text_content = str(asunto)
        html_content = render_to_string('core/email/email.html', context, request=request)

        try:
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, 'text/html')
            msg.send(fail_silently=False)
            messages.success(request, '¡Tu consulta se envió con éxito!')

            contact = Contact(first_name=nombre, last_name=apellido, email=email, tel=telefono, contact_category=categoria, subject=asunto, body=consulta)
            contact.save()
        
        except SMTPException as e:
            print('There was an error sending an email: ', e)
            messages.error(request, 'Hubo un error enviando tu consulta. Volvé a probar más tarde.')
            return render(request, 'core/contact.html')
            
        return render(request, 'core/contact.html')

    return render(request, 'core/contact.html')

def donaciones(request):
    return render(request, 'core/donaciones.html')
