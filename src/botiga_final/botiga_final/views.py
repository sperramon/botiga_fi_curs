# -*- coding: utf-8 -*-
from pyramid.view import view_config
from objecteProducte import Productes

@view_config(route_name='productes', renderer='productes.mako')
def productes_view(request):
   objecteProducte=Productes()
   dades=objecteProducte.agafarProductes()
   return { "productes":dades }
   
@view_config(route_name='fercomanda',renderer='comanda_feta.mako')
def recollir_dades(request):
    objecteEnviar=Productes()
    dadesRecollides=objecteEnviar.captarProductes(request)
    ObjecteEnviar.introduirDades(dadesRecollides)
    return {"recollir":dadesRecollides}

@view_config(route_name='inici', renderer='inici.mako')
def inici_view(request):
   return {"Titol":"Inici"}

@view_config(route_name='comanda', renderer='comanda.mako')
def comanda_view(request):
    objecteProducte=Productes()
    dades=objecteProducte.llegir_comanda()
    return { "productes":dades }

