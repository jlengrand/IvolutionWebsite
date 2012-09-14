#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Julien Lengrand-Lambert"
SITENAME = u"Ivolution"
SITEURL = 'localhost'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

PAGELINKS =  (('Ivolution Project', 'Ivolution.html'),
          ('1 minute kick-off', 'OneMinuteTutorial.html'),
          ('Downloads', 'Downloads.html'),
          ('Installation', 'Installation.html'),
          ('Main Interface', 'MainInterface.html'),
          ('Settings Interface', 'Settings.html'),
          ('Future Developments', 'FutureDevelopments.html'),
          ('About', 'About.html'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
NEWEST_FIRST_ARCHIVES = False

THEME = "ivolution"

#theme folder = /home/test/.virtualenvs/pelican/local/lib/python2.7/site-packages/pelican/themes/svbtle' ...