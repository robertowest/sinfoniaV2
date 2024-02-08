from django.http import HttpResponseRedirect


def Redireccionamiento(request):
    # if request.user is not None and request.user.is_active:
    #     if request.user.is_superuser:
    #         return HttpResponseRedirect("/admin/")

    #     elif request.user.is_staff:
    #         # # si el empleado es un comercial, enviamos hacia otro destino
    #         # # comercial = get_object_or_404(Comercial, usuario=request.user)
    #         # try:
    #         #     comercial = Comercial.objects.get(usuario=request.user)
    #         #     if comercial:
    #         #         # return HttpResponseRedirect("/comercial/")
    #         #         # return HttpResponseRedirect("/empresa/recorrer/")
    #         #         # return HttpResponseRedirect("/empresa/filtro_comercial/" + str(comercial.id))
    #         #         get_args_str = urlencode({'comercial': comercial.id, 'active': True})
    #         #         return HttpResponseRedirect("/empresa/listado/?%s" % get_args_str)
    #         #     else:
    #         #         # return HttpResponseRedirect("/empresa/")
    #         #         return HttpResponseRedirect(reverse('gestion:dashboard'))

    #         # except Comercial.DoesNotExist:
    #         #     return HttpResponseRedirect(reverse('gestion:dashboard'))
    #         return HttpResponseRedirect("/")
    return HttpResponseRedirect('/home/')
