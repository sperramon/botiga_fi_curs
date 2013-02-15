# -*- coding: utf-8 -*-
from pyramid.view import view_config
from objecteProducte import Productes


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'botiga'}


@view_config(route_name='productes', renderer='productes.mako')
def productes_view(request):
   objecteProducte=Productes()
   dades=objecteProducte.agafarProductes()
   return { "productes":dades }

def recollir_dades(request):
    objecteEnviar=Productes()
    dadesRecollides=objecteEnviar.captarProductes()
    ObjecteEnviar.introduirDades(dadesRecollides)
    return {"recollir":dadesRecollides}

