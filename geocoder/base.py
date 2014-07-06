#!/usr/bin/python
# coding: utf8

from __future__ import print_function
import requests
import json


class Base(object):
    base_references = [
        '[GitHub Repo](https://github.com/DenisCarriere/geocoder)',
        '[GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)']

    _exclude = ['parse', 'json', 'url', 'attributes', 'help', 'debug',
                'api', 'description', 'content', 'params', 'status_code',
                'references', 'api_references', 'base_references', 'status_description']
    attributes = []

    def __repr__(self):
        return "<[{0}] {1} [{2}]>".format(self.status, self.provider, self.address)

    def __getattr__(self, item):
        return str('')

    def debug(self):
        print('# Debug')
        print('## Connection')
        print('* URL: [{0}]({1})'.format(self.provider.title(), self.url))
        print('* Status: {0}'.format(self.status))
        print('* Status Code: {0}'.format(self.status_code))
        for key, value in self.params.items():
            print('* Parameter [{0}]: {1}'.format(key, value))
        print('')
        print('## JSON Attributes')
        for key, value in self.json.items():
            print('* {0}: {1}'.format(key, value))
        print('')
        print('## Provider\'s Attributes')
        if self.parse:
            for key, value in self.parse.items():
                try:
                    value = value.encode('utf-8')
                except:
                    pass
                print('* {0}: {1}'.format(key, value))
        else:
            print(self.content)

    def help(self):
        print('# {0}'.format(self.provider))
        print('')
        print(self.description)
        print('Using Geocoder you can retrieve {0}\'s geocoded data from {1}.'.format(self.provider, self.api))
        print('')
        print('## Python Example')
        print('')
        print('```python')
        print('>>> import geocoder')
        print('>>> g = geocoder.{0}(<address>)'.format(self.provider.lower()))
        print('>>> g.lat, g.lng')
        print('45.413140 -75.656703')
        print('...')
        print('```')
        print('')
        print('## Geocoder Attributes')
        print('')
        for attribute in self.attributes:
            print('* {0}'.format(attribute))
        print('')
        print('## References')
        print('')
        for reference in self.base_references + self.api_references:
            print('* {0}'.format(reference))
        print('')

    def _json(self):
        for key in dir(self):
            if bool(not key.startswith('_') and key not in self._exclude):
                self.attributes.append(key)
                value = getattr(self, key)
                if value:
                    self.json[key] = value

    def _connect(self):
        self.status_code = 404
        self.status = 'Connecting...'
        try:
            r = requests.get(self.url, params=self.params)
            self.status_code = r.status_code
            self.url = r.url
            self.status = 'OK'
        except KeyboardInterrupt:
            self.status = 'ERROR - User Quit'
            sys.exit()
        except:
            self.status = 'ERROR - URL Connection'

        # Open JSON content from Request connection
        try:
            self.content = r.json()
        except:
            self.status = 'ERROR - JSON Corrupted'
            self.content = r.content

    def _parse(self, content, last=''):
        # DICTIONARY
        if isinstance(content, dict):
            for key, value in content.items():

                # NOKIA EXCEPTION
                if key in 'AdditionalData':
                    for item in value:
                        key = item.get('key')
                        value = item.get('value')
                        self.parse[key] = value

                # STANDARD DICTIONARY
                if isinstance(value, (list, dict)):
                    self._parse(value, key)
                else:
                    if last:
                        key = '{0}-{1}'.format(last, key)
                    self.parse[key] = value

        # LIST
        elif isinstance(content, list):
            if len(content) == 1:

                self._parse(content[0], last)
            elif len(content) > 1:
                for num, value in enumerate(content):

                    # BING EXCEPTION
                    if not last in ['geocodePoints']:
                        key = '{0}-{1}'.format(last, num)
                    else:
                        key = last
                    if isinstance(value, (list, dict)):
                        self._parse(value, key)
                    else:
                        self.parse[key] = value

    def _test(self):
        if self.status_description:
            self.status = self.status_description
        elif not self.address:
            self.status = 'ERROR - No results found'
        elif not bool(self.lng and self.lat):
            self.status = 'ERROR - No Geometry'
        else:
            self.status = 'OK'


    def _get_json_str(self, item):
        result = self.parse.get(item)
        try:
            return result.encode('utf-8')
        except:
            return str('')

    def _get_json_float(self, item):
        result = self.parse.get(item)
        try:
            return float(result)
        except:
            return 0.0

    def _get_bbox(self, south, west, north, east):
        # South Latitude, West Longitude, North Latitude, East Longitude
        self.south = south
        self.west = west
        self.north = north
        self.east = east

        if bool(south and east and north and west):
            self.southwest = {'lat': south, 'lng': west}
            self.southeast = {'lat': south, 'lng': east}
            self.northeast = {'lat': north, 'lng': east}
            self.northwest = {'lat': north, 'lng': west}
            bbox = {'southwest': self.southwest, 'northeast': self.northeast}
            return bbox
        return str('')

    """
    def load(self, json, last=''):
        # DICTIONARY
        if isinstance(json, dict):
            for keys, values in json.items():
                # Canada Post
                if keys == 'Items':
                    for key, value in values[0].items():
                        if value:
                            self.json[key] = value

                # MAXMIND
                if 'geoname_id' in json:
                    names = json.get('names')
                    self.json[last] = names['en']


                # NOKIA
                if keys in 'AdditionalData':
                    for item in values:
                        key = item.get('key')
                        value = item.get('value')
                        self.json[key] = value

                # GOOGLE
                if keys == 'results':
                    if values:
                        self.load(values[0], keys)

                elif keys == 'address_components':
                    for item in values:
                        short_name = item.get('short_name')
                        long_name = item.get('long_name')
                        all_types = item.get('types')
                        for types in all_types:
                            self.json[types] = short_name
                            self.json[types + '-long_name'] = long_name

                elif keys == 'types':
                    for item in values:
                        name = 'types_{0}'.format(item)
                        self.json[name] = True

                # LIST
                elif isinstance(values, list):
                    if len(values) == 1:
                        self.load(values[0], keys)
                    elif len(values) > 1:
                        for count, value in enumerate(values):
                            name = '{0}-{1}'.format(keys, count)
                            self.load(value, name)

                # DICTIONARY
                elif isinstance(values, dict):
                    self.load(values, keys)
                else:
                    if last:
                        name = '{0}-{1}'.format(last, keys)
                    else:
                        name = keys
                    self.json[name] = values
        # LIST
        elif isinstance(json, (list, tuple)):
            if json:
                self.load(json[0], last)
        # OTHER Formats
        else:
            self.json[last] = json

    def safe_postal(self, item):
        # Full postal code - K1E 1S9
        expression = r"[A-Z]{1}[0-9]{1}[A-Z]{1}[ ]?[0-9]{1}[A-Z]{1}[0-9]{1}"
        # Partial postal code - K1E
        expression += r"([A-Z]{1}[0-9]{1}[A-Z]{1})?"
        pattern = re.compile(expression)
        if item:
            match = pattern.search(item)

            # Canada Pattern
            if match:
                return match.group()
            else:
                # United States Pattern
                pattern = re.compile(r'[0-9]{5}([0-9]{4})?')
                match = pattern.search(item)
                if match:
                    return match.group()
        return None

    def safe_format(self, item):
        item = self.json.get(item)
        if item:
            item = item.encode('utf-8')
        return item

    def safe_coord(self, item):
        item = self.json.get(item)
        if item:
            try:
                return float(item)
            except:
                return None
        else:
            return None

    def safe_bbox(self, south, west, north, east):
        # South Latitude, West Longitude, North Latitude, East Longitude
        try:
            self.south = float(south)
            self.west = float(west)
            self.north = float(north)
            self.east = float(east)
        except:
            self.south = None
            self.west = None
            self.north = None
            self.east = None

        if bool(self.south and self.east and self.north and self.west):
            self.southwest = {'lat': self.south, 'lng': self.west}
            self.southeast = {'lat': self.south, 'lng': self.east}
            self.northeast = {'lat': self.north, 'lng': self.east}
            self.northwest = {'lat': self.north, 'lng': self.west}
            bbox = {'southwest': self.southwest, 'northeast': self.northeast}
            return bbox
        return None

    def debug(self):
        pass


    REMOVE THIS SOON
    @property
    def ok(self):
        return bool(self.lng and self.lat)

    @property
    def status(self):
        if self.lng:
            return 'OK'
        else:
            return 'ERROR - No Geometry'
"""