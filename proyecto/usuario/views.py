from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from allauth.socialaccount.models import SocialAccount

def logIn(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':

        usuario = request.POST.get('usuario')
        contra = request.POST.get('contraseña')

        if usuario == "" or contra == "":
            return HttpResponse("All fields required")

        user = authenticate(username=usuario, password=contra)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            message = "Este usuario no existe. Verificá si ingresaste tu nombre de usuario o contraseña correctamente."
            return render(request, 'login.html', {'message':message})
    
    return render(request, 'login.html')

def registro(request):

    if request.user.is_authenticated:
        return redirect('/')

    form = RegistroForm()

    if request.method == 'POST':

        form = RegistroForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            return redirect('iniciar-sesion')

    return render(request, 'register.html', {'form' : form})

def logOut(request):

    if not request.user.is_authenticated:
        return redirect('/')

    logout(request)

    return redirect('/')

def change_pass(request):

    socialaccount = SocialAccount.objects.all()
    accounts_list = []
    for i in socialaccount:
        accounts_list.append(i.user.username)

    if not request.user.is_authenticated or request.user.username in accounts_list:
        return redirect('/')

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '¡Tu contraseña fué actualizada con éxito!')
            return redirect('cambiar-contraseña')
        else:
            messages.error(request, 'Por favor, verificá si ingresaste bien los datos.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password/change/change_pass.html', {
        'form': form
    })