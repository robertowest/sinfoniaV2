from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.http import urlencode

from .forms import LoginForm, SignUpForm


def LoginRedirect(request):
    return HttpResponseRedirect("/")


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            userinput = request.POST['username']
            try:
                username = User.objects.get(email=userinput).username
            except User.DoesNotExist:
                username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                # return redirect('users:redirect')
                return redirect('/')
            else:
                msg = 'Credenciales incorrectas.'
                messages.error(request, 'Datos incorrectos, por favor verifique usuario/correo o contraseña.')
        else:
            msg = 'Error al validar el formulario'
            messages.error(request, 'Datos incorrectos, por favor verifique los datos cargados.')

    return render(request, "users/login.html", {"form": form, "msg": msg})
    

def register_user(request):
    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Usuario creado - por favor, <a href="/login">inicie sesión</a>.'
            success = True
        else:
            msg = 'Los datos del formulario no son válidos.'
    else:
        form = SignUpForm()

    return render(request, "users/register.html", {"form": form, "msg" : msg, "success" : success })
