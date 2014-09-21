#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import bing_key
from .location import Location


class BingReverse(Base):
    provider = 'bing'
    api = 'Bing Maps REST Services'
    url = 'http://dev.virtualearth.net/REST/v1/Locations'
    _description = 'The Bing™ Maps REST Services Application Programming Interface (API)\n'
    _description += 'provides a Representational State Transfer (REST) interface to\n'
    _description += 'perform tasks such as creating a static map with pushpins, geocoding\n'
    _description += 'an address, retrieving imagery metadata, or creating a route.'
    _api_reference = ['[{0}](http://msdn.microsoft.com/en-us/library/ff701714.aspx)'.format(api)]
    _api_parameter  = [':param ``key``: (optional) use your own API Key from Bing.']

    def __init__(self, location, key=bing_key):
        self.location = location
        g = Location(location)
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['key'] = key
        self.params['o'] = 'json'
        self.url = self.url + '/{0},{1}'.format(g.lat, g.lng)

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()

    @property
    def status_description(self):
        return self._get_json_str('statusDescription')

    @property
    def lat(self):
        return self._get_json_float('coordinates-0')

    @property
    def lng(self):
        return self._get_json_float('coordinates-1')

    @property
    def route(self):
        return self._get_json_str('address-addressLine')

    @property
    def address(self):
        return self._get_json_str('address-formattedAddress')

    @property
    def quality(self):
        return self._get_json_str('resources-entityType')

    @property
    def accuracy(self):
        return self._get_json_str('geocodePoints-calculationMethod')

    @property
    def postal(self):
        return self._get_json_str('address-postalCode')

    @property
    def bbox(self):
        south = self._get_json_float('bbox-0')
        north = self._get_json_float('bbox-2')
        west = self._get_json_float('bbox-1')
        east = self._get_json_float('bbox-3')
        return self._get_bbox(south, west, north, east)

    @property
    def locality(self):
        return self._get_json_str('address-locality')

    @property
    def state(self):
        return self._get_json_str('address-adminDistrict')

    @property
    def country(self):
        return self._get_json_str('address-countryRegion')

if __name__ == '__main__':
    g = Bing('453 Booth Street, Ottawa ON')
    g.help()
    g.debug()