from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('iniciar-sesion/', views.logIn, name='iniciar-sesion'),
    path('cerrar-sesion/', views.logOut, name='cerrar-sesion'),
    path('registro/', views.registro, name='registro'),

    # Cambio de contraseña

    path('cambiar-contraseña/', views.change_pass, name="cambiar-contraseña"),

    # Reseteo de contraseña

    path('reset', auth_views.PasswordResetView.as_view(template_name="password/reset/reset_pass_form.html", html_email_template_name="password/reset/reset_pass_email.html", subject_template_name="password/reset/reset_pass_email_subject.txt", title="Restablecer contraseña"), name="password_reset"),
    path('reset/done',auth_views.PasswordResetDoneView.as_view(template_name="password/reset/reset_pass_finish.html", title="Correo enviado"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password/reset/reset_pass_confirm.html", title="Nueva Contraseña"), name='password_reset_confirm'),
    path('reset/completed', auth_views.PasswordResetCompleteView.as_view(template_name="password/reset/reset_pass_completed.html", title="Finalizado"), name='password_reset_complete'),

]
