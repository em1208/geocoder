Geocoder
========

.. image:: https://badge.fury.io/py/geocoder.png
    :target: http://badge.fury.io/py/geocoder

.. image:: https://pypip.in/d/geocoder/badge.png
    :target: https://pypi.python.org/pypi/geocoder/

A simplistic Python Geocoder.

Geocoder is an Apache2 Licensed Geocoding library, written in Python.

.. code-block:: pycon

    >>> g = geocoder.google('Parliament Hill, Ottawa')
    >>> g.latlng
    [45.4235937, -75.700929]
    >>> g.latitude
    45.4235937
    >>> g.address
    'Parliament Hill, Wellington Street, Ottawa, ON, Canada'

Installation
------------

To install Geocoder, simplpy:

.. code-block:: bash

    $ pip install geocoder


Geocoding Providers
-------------------

- Google
- Bing
- TomTom
- Nokia
- Mapquest
- OSM
- ESRI
- Geolytica
- MaxMind


Documentation
-------------
    
Basic Usage
```````````

.. code-block:: pycon

    >>> import geocoder
    >>> g = geocoder.osm('1600 Amphitheatre Pkwy, Mountain View, CA')
    >>> g.xy
    [-122.0850862, 37.4228139]
    >>> g.postal
    '94043'
    >>> g.address
    'Google Headquaters, 1600, Amphitheatre Parkway, Mountain View...'
    >>> g.bbox
    [(37.4228134155273, -122.085090637207), (37.4228172302246, -122.085083007812)]
    # bbox = [SouthWest, NorthEast]
    >>> g.quality
    'commercial'
    >>> g.x, g.y
    (-122.0850862, 37.4228139)
    >>> g.south, g.west
    (37.4228134155273, -122.085090637207)
    ...

Geocoding IP Address
````````````````````

.. code-block:: pycon

    >>> g = geocoder.maxmind('74.125.226.99')
    >>> g
    <[OK] Geocoder MaxMind [Mountain View, California United States]>
    >>> g.xy
    [-122.0574, 37.4192]
    ...

Using Proxies
`````````````

.. code-block:: pycon 

    >>> proxy = {'http':'http://78.130.201.110:8080'}
    >>> g = geocoder.google('Ottawa, Ontario', proxy=proxy)
    ...

Geocoding Providers
```````````````````

.. code-block:: pycon

    >>> geocoder.google(<location>)
    >>> geocoder.tomtom(<location>)
    >>> geocoder.mapquest(<location>)
    >>> geocoder.nokia(<location>)
    >>> geocoder.esri(<location>)
    >>> geocoder.maxmind(<location>)
    >>> geocoder.bing(<location>)
    >>> geocoder.osm(<location>)
    >>> geocoder.mapquest(<location>)
    ...


Contribute
----------

Please feel free to give any feedback on this module, it is still in it's early stages of production. If you have any questions about GIS & Python you can contact @DenisCarriere for any questions.

.. _`the repository`: https://github.com/DenisCarriere/geocoder.git


.. image:: https://d2weczhvl823v0.cloudfront.net/DenisCarriere/geocoder/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

