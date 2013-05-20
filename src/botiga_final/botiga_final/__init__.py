# -*- coding: utf-8 -*-
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .security import groupfinder    
from .models import RootFactory
import os

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    settings['mako.directories'] = os.path.join(here, 'templates')
    #config = Configurator(settings=settings)//
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(root_factory='.models.RootFactory', settings=settings)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    #
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('inici', '/') #productes=view, /botiga = URL
    config.add_route('productes', '/productes') #productes=view, /botiga = URL
    config.add_route('comanda', '/comanda') #productes=view, /botiga = URL
    config.add_route('fercomanda', '/comanda_feta') #productes=view, /botiga = URL
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.scan()
    return config.make_wsgi_app()
