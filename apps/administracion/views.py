import requests
from django.shortcuts import render

from . import models


def index(request):
    context = {}
    return render(request, 'administracion/index.html', context)



# def obtener_remesas(request):
#     response = requests.get('https://randomuser.me/api')
#     if response.status_code == 200:
#         remesas = response.json()
#     else:
#         remesas = []
#     return render(request, 'recepcion/remesas.html', {'remesas': remesas})
def obtener_remesas(request):
    # # obtenemos un json
    # titles = {'data': [{'id': '20ad5d9c-b32e-4599-8866-a3aaa5ac77de','name': 'name_1'},
    #                    {'id': '7b6d76cc-86cd-40f8-be90-af6ced7fec44','name': 'name_2'},
    #                    {'id': 'b8843b1a-9eb0-499f-ba64-25e436f04c4b','name': 'name_3'}]}

    # # Create a Django model object for each object in the JSON 
    # for title in titles['data']:
    #     models.Remesa.objects.create(id=title['id'], name=title['name'])
    # return render(request, 'recepcion/remesas.html', {'remesas': models.Remesa.objects.all()})
    return render(request, 'administracion/remesas.html', {'remesas': []})
