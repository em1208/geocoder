#!/usr/bin/python
# coding: utf8

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
from timezone import Timezone
from elevation import Elevation
from geolytica import Geolytica
from canadapost import Canadapost


def geolytica(location):
    """
    # Geolytica

    Geocoder.ca - A Canadian and US location geocoder.
    Using Geocoder you can retrieve Geolytica's geocoded data from Geocoder.ca.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.geolytica(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * lat
        * lng
        * locality
        * location
        * postal
        * provider
        * route
        * state
        * status
        * street_number

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Geocoder.ca](http://geocoder.ca/?api=1)

    """
    return Geolytica(location)

def bing(location, key=bing_key):
    """
    # Bing

    The Bing Maps REST Services Application Programming Interface (API)
    provides a Representational State Transfer (REST) interface to perform
    tasks such as creating a static map with pushpins, geocoding an address,
    retrieving imagery metadata, or creating a route.
    Using Geocoder you can retrieve Bing's geocoded data from Bing Maps REST Services.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.bing(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * country
        * lat
        * lng
        * locality
        * location
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * status_description

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Bing Maps REST Services](http://msdn.microsoft.com/en-us/library/ff701714.aspx)

    """
    return Bing(location, key=key)

def nokia(location, app_id=app_id, app_code=app_code):
    """
    # Nokia

    Send a request to the geocode endpoint to find an address using a combination of
    country, state, county, city, postal code, district, street and house number.
    Using Geocoder you can retrieve Nokia's geocoded data from HERE Geocoding REST API.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.nokia(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * accuracy
        * address
        * bbox
        * country
        * county
        * lat
        * lng
        * locality
        * location
        * neighborhood
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * street_number

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [HERE Geocoding REST API](https://developer.here.com/rest-apis/documentation/geocoder)

    """
    return Nokia(location, app_id=app_id, app_code=app_code)

def tomtom(location, key=tomtom_key):
    """
    # TomTom

    The Geocoding API gives developers access to TomTom’s first class geocoding service.
    Developers may call this service through either a single or batch geocoding request.
    This service supports global coverage, with house number level matching in over 50 countries,
    and address point matching where available.
    Using Geocoder you can retrieve TomTom's geocoded data from Geocoding API.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.tomtom(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * country
        * lat
        * lng
        * locality
        * location
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * street_number

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Geocoding API](http://developer.tomtom.com/products/geocoding_api)

    """
    return Tomtom(location, key=key)

def mapquest(location):
    """
    # MapQuest

    The geocoding service enables you to take an address and get the
    associated latitude and longitude. You can also use any latitude
    and longitude pair and get the associated address. Three types of
    geocoding are offered: address, reverse, and batch.
    Using Geocoder you can retrieve MapQuest's geocoded data from Geocoding Service.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.mapquest(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * country
        * lat
        * lng
        * locality
        * location
        * postal
        * provider
        * quality
        * state
        * status

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Geocoding Service](http://www.mapquestapi.com/geocoding/)

    """
    return Mapquest(location)

def osm(location):
    """
    # OSM

    Nominatim (from the Latin, 'by name') is a tool to search OSM data by name
    and address and to generate synthetic addresses of OSM points (reverse geocoding).
    Using Geocoder you can retrieve OSM's geocoded data from Nominatim.

    ## Python Example

        >>> import geocoder
        >>> g = geocoder.osm(<address>)
        >>> g.lat, g.lng
        45.413140 -75.656703
        ...

    ## Geocoder Attributes

        * address
        * bbox
        * country
        * lat
        * lng
        * locality
        * location
        * neighborhood
        * postal
        * provider
        * quality
        * route
        * state
        * status
        * street_number
        * suburb

    ## References

        * [GitHub Repo](https://github.com/DenisCarriere/geocoder)
        * [GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)
        * [Nominatim](http://wiki.openstreetmap.org/wiki/Nominatim)

    """
    return Osm(location)

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


def timezone(latlng, timestamp='', proxies='', timeout=5.0):
    """
    Timezone tool will retrieve the zone & offset of a desired location
    using Google's Time Zone API.

    The UTC (Coordinated Universal Time) and the DST (Daylight Savings Time)
    results are in seconds.

        >>> g = geocoder.timezone("Ottawa")
        >>> g.timezone
        Eastern Daylight Time
        >>> g.timezone_id
        America/Toronto
        >>> g.utc
        -18000
        >>> g.dst
        3600
        ...

    Official Docs
    -------------
    https://developers.google.com/maps/documentation/timezone/
    """
    provider = Timezone(latlng)
    return Geocoder(provider, proxies=proxies, timeout=timeout)

def elevation(latlng, proxies='', timeout=5.0):
    """
    Elevation tool will return the Mean elevation above Sea Level in meters based
    on Lat & Lng inputs or an address using Google's elevation API.

        >>> latlng = (37.4192, -122.0574)
        >>> g = geocoder.elevation(latlng)
        OR
        >>> g = geocoder.elevation("Ottawa")
        >>> g.meters
        '71.8'
        ...

    Official Docs
    -------------
    https://developers.google.com/maps/documentation/elevation/
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