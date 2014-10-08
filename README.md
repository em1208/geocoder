# [Geocoder](https://github.com/DenisCarriere/geocoder) [![version](https://badge.fury.io/py/geocoder.png)](http://badge.fury.io/py/geocoder) [![build](https://travis-ci.org/DenisCarriere/geocoder.png?branch=master)](https://travis-ci.org/DenisCarriere/geocoder)

### A complete Python Geocoding module made easy.

Every task is made easy with tons of ``help`` & ``debug`` commands!

```python
>>> import geocoder # pip install geocoder
>>> g = geocoder.google('<address>')
>>> g.lat, g.lng
45.413140 -75.656703
...
```

![Providers](https://pbs.twimg.com/media/Bqi8kThCUAAboo0.png)

## QuickStart

A place to get you started on how to use this module and set up your work station.

**Install from PyPi**
```bash
$ pip install geocoder
```

## Command Line Interface

The command line tool allows you to geocode one or many strings, either
passed as an argument, passed via STDIN, or contained in a referenced file.

```bash
$ geocode "Ottawa"
{
  "accuracy": "Rooftop",
  "quality": "PopulatedPlace",
  "lng": -75.68800354003906,
  "status": "OK",
  "locality": "Ottawa",
  "country": "Canada",
  "provider": "bing",
  "state": "ON",
  "location": "Ottawa",
  "address": "Ottawa, ON",
  "lat": 45.389198303222656
}
```

Now, suppose you have a file with two lines, which you want to geocode.

```bash
$ geocode `textfile.txt`
{"status": "OK", "locality": "Ottawa", ...}
{"status": "OK", "locality": "Boston", ...}
```

The output is, by default, sent to stdout, so it can be conveniently parsed
by json parsing tools like `jq`.

```bash
$ geocode `textfile.txt` | jq [.lat,.lng,.country] -c
[45.389198303222656,-75.68800354003906,"Canada"]
[42.35866165161133,-71.0567398071289,"United States"]
```

For more development requests for the CLI, please provide your input in the [Github Issues Page](https://github.com/DenisCarriere/geocoder/issues).

### Visit the [Wiki](https://github.com/DenisCarriere/geocoder/wiki/)

Please look at the following pages on the wiki for more information about a certain topic.

### Providers
Here is a list of providers that are available for use with **FREE** or limited restrictions.

- **[OSM](https://github.com/DenisCarriere/geocoder/wiki/OSM)**

- **[Bing](https://github.com/DenisCarriere/geocoder/wiki/Bing)**

- **[Nokia](https://github.com/DenisCarriere/geocoder/wiki/Nokia)**

- **[Yahoo](https://github.com/DenisCarriere/geocoder/wiki/Yahoo)**

- **[Google](https://github.com/DenisCarriere/geocoder/wiki/Google)**

- **[ArcGIS](https://github.com/DenisCarriere/geocoder/wiki/ArcGIS)**

- **[TomTom](https://github.com/DenisCarriere/geocoder/wiki/TomTom)**

- **[Geonames](https://github.com/DenisCarriere/geocoder/wiki/Geonames)**

- **[MapQuest](https://github.com/DenisCarriere/geocoder/wiki/MapQuest)**

- **[Geocoder.ca](https://github.com/DenisCarriere/geocoder/wiki/Geocoder.ca)**

### Extras

The fun extra stuff I added to enjoy some cool features the web has to offer.

- **[Reverse Geocoding](https://github.com/DenisCarriere/geocoder/wiki/Reverse)**

- **[IP Address](https://github.com/DenisCarriere/geocoder/wiki/IP Address)**

- **[Elevation (Meters)](https://github.com/DenisCarriere/geocoder/wiki/Elevation)**

- **[Time Zone](https://github.com/DenisCarriere/geocoder/wiki/TimeZone)**

- **[CanadaPost](https://github.com/DenisCarriere/geocoder/wiki/CanadaPost)**


### Topic not available?

If you cannot find a topic you are looking for, please feel free to ask me [@DenisCarriere](https://github.com/DenisCarriere) or post them on the [Github Issues Page](https://github.com/DenisCarriere/geocoder/issues).

## Support

This project is free & open source, it would help greatly for you guys reading this to contribute, here are some of the ways that you can help make this Python Geocoder better.

### Feedback

Please feel free to give any feedback on this module. If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the [Github Issues Page](https://github.com/DenisCarriere/geocoder/issues).

### Twitter

Speak up on Twitter [@Addxy](https://twitter.com/search?q=%40Addxy) and tell us how you use this Python Geocoder. New updates will be pushed to Twitter Hashtags [#geocoder](https://twitter.com/search?q=%23geocoder).

### Thanks to

A big thanks to all the people that help contribute: [@flebel](https://github.com/flebel) [@patrickyan](https://github.com/patrickyan)
