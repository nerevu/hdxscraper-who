# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab

"""
config
~~~~~~

Provides app configuration settings
"""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

from os import path as p

BASEDIR = p.dirname(__file__)
PARENTDIR = p.dirname(BASEDIR)
DB_NAME = 'scraperwiki.sqlite'
RECIPIENT = 'reubano@gmail.com'


class Config(object):
    BASE_URL = 'http://apps.who.int/gho/athena/data/GHO/CC_1,CC_2,CC_3,CC_4,CC_5,CC_6,CC_7,CC_8.json?profile=simple&filter=COUNTRY:-;REGION:*'
    LOCATION = 'fact.item'
    KEY = 'indicator'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % p.join(BASEDIR, DB_NAME)
    LOGFILE = p.join(BASEDIR, 'http', 'log.txt')
    API_LIMIT = 1000
    SW = False
    DEBUG = False
    TESTING = False
    PROD = False
    CHUNK_SIZE = 2 ** 14
    ROW_LIMIT = None


class Scraper(Config):
    PROD = True
    SW = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % p.join(PARENTDIR, DB_NAME)
    LOGFILE = p.join(PARENTDIR, 'http', 'log.txt')


class Production(Config):
    PROD = True


class Development(Config):
    DEBUG = True
    ROW_LIMIT = 50


class Test(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG = True
    ROW_LIMIT = 10
    TESTING = True
