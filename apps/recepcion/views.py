from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'recepcion/index.html', context)
