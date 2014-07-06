#!/usr/bin/python
# coding: utf8

from base import Base
from keys import tomtom_key

class Tomtom(Base):

    provider = 'TomTom'
    api = 'Geocoding API'
    url = 'https://api.tomtom.com/lbs/geocoding/geocode'
    api_references = ['[{0}](http://developer.tomtom.com/products/geocoding_api)'.format(api)]
    description = 'The Geocoding API gives developers access to TomTom’s first class geocoding service. \n'
    description += 'Developers may call this service through either a single or batch geocoding request.\n'
    description += 'This service supports global coverage, with house number level matching in over 50 countries,\n'
    description += 'and address point matching where available.'

    def __init__(self, location, key=tomtom_key):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['key'] = key
        self.params['query'] = location
        self.params['format'] = 'json'
        self.params['maxResults'] = 1

        # Initialize
        self._connect()
        self._parse(self.content)
        self._test()
        self._json()

    @property
    def lat(self):
        return self._get_json_float('geoResult-latitude')

    @property
    def lng(self):
        return self._get_json_float('geoResult-longitude')

    @property
    def street_number(self):
        return self._get_json_str('geoResult-houseNumber')

    @property
    def route(self):
        return self._get_json_str('geoResult-street')

    @property
    def address(self):
        return self._get_json_str('geoResult-formattedAddress')

    @property
    def quality(self):
        return self._get_json_str('geoResult-type')

    @property
    def postal(self):
        return self._get_json_str('geoResult-postcode')

    @property
    def locality(self):
        return self._get_json_str('geoResult-city')

    @property
    def state(self):
        return self._get_json_str('geoResult-state')

    @property
    def country(self):
        return self._get_json_str('geoResult-country')

    @property
    def quality(self):
        return self._get_json_str('geoResult-type')


if __name__ == '__main__':
    g = Tomtom('453 Booth Street, Ottawa')
    g.help()
    g.debug()