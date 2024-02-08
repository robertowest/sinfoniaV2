from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                msg = 'Credenciales inválidas'
        else:
            msg = 'Error al validar el formulario'

    return render(request, 'registration/login.html', {'form': form, 'msg': msg})

def register_user(request):
    msg = None
    success = False

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            msg = 'Cuenta nueva, favor de <a href="/login">iniciar sesión</a>.'
            success = True

            # return redirect('/login/')

        else:
            msg = 'Error al validar el formulario'
    else:
        form = SignUpForm()

    return render(request, 'accounts/register.html', {'form': form, 'msg': msg, 'success': success})

def profile(request):
    return render(request, 'registration/profile.html')