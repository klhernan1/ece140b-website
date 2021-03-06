from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import FileResponse
import mysql.connector as mysql
import os
from wsgiref.simple_server import make_server


def costs_page(req):
    return FileResponse("templates/costs.html")


def features_page(req):
    return FileResponse("templates/features.html")


def interaction_page(req):
    return FileResponse("templates/interaction.html")


def kvp_page(req):
    return FileResponse("templates/kvp.html")


def notes_page(req):
    return FileResponse("templates/notes.html")


def product_page(req):
    return FileResponse("templates/product.html")


def pivot_page(req):
    return FileResponse("templates/pivot.html")


def revenue_page(req):
    return FileResponse("templates/revenue.html")


def home_page(req):
    return FileResponse("templates/home.html")


if __name__ == '__main__':
    with Configurator() as config:

        config.add_route('costs', '/costs')
        config.add_view(costs_page, route_name='costs')

        config.add_route('home', '/')
        config.add_view(home_page, route_name='home')

        config.add_route('features', '/features')
        config.add_view(features_page,
                        route_name='features')

        config.add_route('interaction', '/interaction')
        config.add_view(interaction_page,
                        route_name='interaction')

        config.add_route('kvp', '/kvp')
        config.add_view(kvp_page, route_name='kvp', renderer='json')

        config.add_route('notes', '/notes')
        config.add_view(notes_page, route_name='notes', renderer='json')

        config.add_route('pivot', '/pivot')
        config.add_view(pivot_page, route_name='pivot')

        config.add_route('product', '/product')
        config.add_view(product_page, route_name='product', renderer='json')

        config.add_route('revenue', '/revenue')
        config.add_view(revenue_page,
                        route_name='revenue')

        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6000, app)
    server.serve_forever()
