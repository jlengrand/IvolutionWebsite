#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Julien Lengrand-Lambert"
SITENAME = u"Ivolution"
SITEURL = 'http://jlengrand.github.com/Ivolution'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Python.org', 'http://python.org'),
          ('OpenCV', 'http://opencv.willowgarage.com/wiki/'),
          ('WxPython', 'http://wxpython.org/'),)

PAGELINKS =  (('Ivolution Project', 'Ivolution.html'),
          ('One minute tutorial', 'OneMinuteTutorial.html'),
          ('Downloads', 'Downloads.html'),
          ('Installation', 'Installation.html'),
          ('Main Interface', 'MainInterface.html'),
          ('Settings', 'Settings.html'),
          ('FAQ', 'FAQ.html'),
          ('Future Developments', 'FutureDevelopments.html'),
          ('About', 'About.html'),)

# Social widget
SOCIAL = (('My website', 'http://lengrand.fr'),
          ('twitter', 'https://twitter.com/jlengrand'),
          ('Google+', 'https://plus.google.com/u/0/107343304730454368817/posts'),
          ('Github', 'https://github.com/jlengrand'),
          ('Stack Overflow', 'http://stackoverflow.com/users/282677/jlengrand'),
          ('linkedin', 'http://nl.linkedin.com/pub/julien-lengrand-lambert/14/660/551/en'),)

DEFAULT_PAGINATION = False
NEWEST_FIRST_ARCHIVES = False

#theme folder = /home/test/.virtualenvs/pelican/local/lib/python2.7/site-packages/pelican/themes/
THEME = "ivolution"

PLUGINS=['pelican.plugins.sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.8
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'daily'
    }
}

GOOGLE_ANALYTICS = "UA-34919152-1"