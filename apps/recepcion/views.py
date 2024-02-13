import requests
from django.shortcuts import render

from . import models


def index(request):
    context = {}
    return render(request, 'recepcion/index.html', context)
