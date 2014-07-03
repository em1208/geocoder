#!/usr/bin/python
# coding: utf8

import utils
from keys import *
from ip import Ip
from osm import Osm
from bing import Bing
from nokia import Nokia
from arcgis import Arcgis
from tomtom import Tomtom
from google import Google
from reverse import Reverse
from geonames import Geonames
from mapquest import Mapquest
from geocoder import Geocoder
from elevation import Elevation
from geolytica import Geolytica
from canadapost import Canadapost


def google(location, short_name=True, timeout=5.0, proxies='', client='', secret='', api_key=''):
    """
    Retrieves geocoding data from Google's geocoding API V3

        >>> g = geocoder.google('1600 Amphitheatre Pkwy, Mountain View, CA')
        >>> g.latlng
        (37.784173, -122.401557)
        >>> g.country
        'United States'
        ...

    Official Docs
    -------------
    https://developers.google.com/maps/documentation/geocoding/
    """
    provider = Google(location, short_name=short_name, client=client, secret=secret, api_key=api_key)
    return Geocoder(provider, proxies=proxies, timeout=timeout)


def get(location, provider='google', proxies='', short_name=True, timeout=5.0):
    """
    Retrieves geocoding data from Google's geocoding API V3

        >>> g = geocoder.search('123 Address', provider='google')
        >>> g.latlng
        (37.784173, -122.401557)
        >>> g.country
        'United States'
        ...
    """
    provider = utils.get_provider(location, provider=provider, short_name=short_name)
    return Geocoder(provider, proxies=proxies, timeout=timeout)

def ip(location, proxies='', timeout=5.0):
    """
    Geocodes an IP address using MaxMind's services.

        >>> g = geocoder.ip('74.125.226.99')
        >>> g.latlng
        (37.4192, -122.0574)
        >>> g.address
        'Mountain View, California United States'
        ...

    Official Docs
    -------------
    http://www.maxmind.com/en/geolocation_landing
    """
    provider = Ip(location)
    return Geocoder(provider, proxies=proxies, timeout=timeout)


def elevation(latlng, proxies='', timeout=5.0):
    """
    Elevation tool will return the Mean elevation above Sea Level in meters based
    on Lat & Lng inputs or an address using Google's elevation API.

        >>> latlng = (37.4192, -122.0574)
        >>> g = geocoder.elevation(latlng)
        OR
        >>> g = geocoder.elevation("Ottawa")
        >>> g.elevation
        '71.8073501587'
        ...

    Official Docs
    -------------
    https://developers.google.com/maps/documentation/geocoding/
    """
    provider = Elevation(latlng)
    return Geocoder(provider, proxies=proxies, timeout=timeout)


def reverse(latlng, short_name=True, proxies='', timeout=5.0):
    """
    Reverse geocodes a location based on Lat & Lng inputs
    using Google's reverse geocoding API V3.

        >>> latlng = (37.4192, -122.0574)
        >>> g = geocoder.reverse(latlng)
        >>> g.address
        'Sevryns Road, Mountain View, CA 94043, USA'
        >>> g.postal
        '94043'
        ...

    Official Docs
    -------------
    https://developers.google.com/maps/documentation/geocoding/
    """
    provider = Reverse(latlng, short_name=short_name)
    return Geocoder(provider, proxies=proxies, timeout=timeout)



def canadapost(location, country='CA', api_key=canadapost_key, proxies='', timeout=5.0):
    """
    Retrieves geocoding data from Canada Post's data using Address Complete API.

        >>> g = geocoder.canadapost('453 Booth Street, Ottawa ON')
        >>> g.postal
        'K1R 7K9'
        ...

    USA address simply add the country field to the search request.
        >>> g = geocoder.canadapost('843 Burg St, Granville, OH', country='USA')
        >>> g.postal
        '43023-1079'
        ...

    Official Docs
    -------------
    https://www.canadapost.ca/pca
    """
    provider = Canadapost(location, country=country, api_key=api_key)
    return Geocoder(provider, proxies=proxies, timeout=timeout)

def geolytica(location, proxies='', timeout=5.0):
    """
    Retrieves geocoding data from Geocoder.ca data.

        >>> g = geocoder.geolytica('Tacloban City')
        >>> g.latlng
        (11.2430274, 125.0081402)
        >>> g.country
        'Philippines'
        ...

    Official Docs
    -------------
    http://geocoder.ca/?api=1
    """
    provider = Geolytica(location)
    return Geocoder(provider, proxies=proxies, timeout=timeout)

def osm(location, proxies='', timeout=5.0):
    """
    Retrieves geocoding data from OSM's data using Nominatim's geocoding API.

        >>> g = geocoder.osm('Tacloban City')
        >>> g.latlng
        (11.2430274, 125.0081402)
        >>> g.country
        'Philippines'
        ...

    Official Docs
    -------------
    http://wiki.openstreetmap.org/wiki/Nominatim
    """
    provider = Osm(location)
    return Geocoder(provider, proxies=proxies, timeout=timeout)


def arcgis(location, proxies='', timeout=5.0):
    """
    Retrieves geocoding data from ArcGIS's REST geocoding API.

        >>> g = geocoder.arcgis('380 New York St, Redlands, California')
        >>> g.latlng
        (34.05649072776595, -117.19566584280369)
        >>> g.postal
        '92373'
        ...

    Official Docs
    -------------
    http://resources.arcgis.com/en/help/arcgis-rest-api/
    """
    provider = Arcgis(location)
    return Geocoder(provider, proxies=proxies, timeout=timeout)


def mapquest(location, proxies='', timeout=5.0):
    """
    Retrieves geocoding data from MapQuest's address geocoding API.

        >>> g = geocoder.mapquest('1555 Blake street, Denver')
        >>> g.latlng
        (39.740009, -104.992264)
        >>> g.quality
        'CITY'
        ...

    Official Docs
    -------------
    http://www.mapquestapi.com/geocoding/
    """
    provider = Mapquest(location)
    return Geocoder(provider, proxies=proxies, timeout=timeout)


def tomtom(location, key=tomtom_key, proxies='', timeout=5.0):
    """
    Retrieves geocoding data from TomTom's geocoding API.

        >>> key = 'XXXXX'
        >>> g = geocoder.tomtom('Amsterdam, Netherlands', key=key)
        >>> g.latlng
        (52.373166, 4.89066)
        >>> g.quality
        'city'
        ...

    Official Docs
    -------------
    http://developer.tomtom.com/products/geocoding_api
    """
    provider = Tomtom(location, key=key)
    return Geocoder(provider, proxies=proxies, timeout=timeout)


def bing(location, key=bing_key, proxies='', timeout=5.0):
    """
    Retrieves geocoding data from Bing's REST location API.

        >>> key = 'XXXXX'
        >>> g = geocoder.bing('Medina, Washington', key=key)
        >>> g.latlng
        (47.615821838378906, -122.23892211914062)
        >>> g.country
        'United States'
        ...

    Official Docs
    -------------
    http://msdn.microsoft.com/en-us/library/ff701714.aspx
    """
    provider = Bing(location, key=key)
    return Geocoder(provider, proxies=proxies, timeout=timeout)


def nokia(location, app_id=app_id, app_code=app_code, proxies='', timeout=5.0):
    """
    Retrieves geocoding data from Nokia's HERE geocoder API.

        >>> app_id = 'XXXXX'
        >>> app_code = 'XXXXX'
        >>> g = geocoder.nokia('Keilaniemi, Espoo')
        >>> g.latlng
        (60.1759338, 24.8327808)
        >>> g.country
        'FIN'
        ...

    Official Docs
    -------------
    https://developer.here.com/rest-apis/documentation/geocoder
    """
    provider = Nokia(location, app_id=app_id, app_code=app_code)
    return Geocoder(provider, proxies=proxies, timeout=timeout)


def geonames(location, username=username, proxies='', timeout=5.0):
    """
    Retrieves geocoding data from Geonames's Web Service API.

        >>> username = 'XXXXX'
        >>> g = geocoder.geonames('Springfield, Virginia', username=username)
        >>> g.latlng
        (38.78928, -77.1872)
        >>> g.country
        'United States'
        >>> g.population
        30484
        ...

    Official Docs
    -------------
    http://www.geonames.org/export/web-services.html
    """
    provider = Geonames(location, username=username)
    return Geocoder(provider, proxies=proxies, timeout=timeout)


def population(location, username=username, proxies='', timeout=5.0):
    """
    Retrieves the population data from Geonames's Web Service API.

        >>> username = 'XXXXX'
        >>> pop = geocoder.population('Springfield, Virginia')
        >>> pop
        30484
        ...

    Official Docs
    -------------
    http://www.geonames.org/export/web-services.html
    """
    g = geonames(location, username=username, proxies=proxies, timeout=timeout)
    return g.pop

if __name__ == '__main__':
    a = (45.4215296, -75.69719309999999)
    g = reverse(a)
    print g