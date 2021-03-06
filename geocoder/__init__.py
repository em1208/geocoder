#!/usr/bin/python
# coding: utf8

"""
geocoder library
~~~~~~~~~~~~~~~~

A pure Python Geocoding module made easy.

Every task is made easy with tons of ``help`` & ``debug`` commands!

    >>> import geocoder # pip install geocoder
    >>> g = geocoder.google('<address>')
    >>> g.lat, g.lng
    45.413140 -75.656703
    ...

"""

__title__ = 'geocoder'
__author__ = 'Denis Carriere'
__version__ = '0.8.4'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Denis Carriere'

# CORE
from .api import yahoo, bing, geonames, google, mapquest, nokia, osm, tomtom, geolytica, arcgis, opencage

# EXTRAS
from .api import ip, canadapost, timezone, elevation, get, location

from cli import cli
