from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'home/index.html', context)

def dashboard(request):
    return render(request, 'home/dashboard.html')

def icons(request):
    return render(request, 'examples/icons.html')

def google(request):
    return render(request, 'examples/map.html')

def profile(request):
    return render(request, 'examples/profile.html')

def tables(request):
    return render(request, 'examples/tables.html')

def login(request):
    return render(request, 'examples/login.html')

def register(request):
    return render(request, 'examples/register.html')
