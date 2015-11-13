#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab

"""
utils
~~~~~

Provides miscellaneous utility methods
"""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

import requests

from ijson import items


def get_records(**kwargs):
    """Fetches json from url"""
    url = kwargs['BASE_URL']
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url, stream=True, headers=headers)
    facts = items(r.raw, kwargs['LOCATION'])

    for fact in facts:
        record = {
            'region': fact['dim']['REGION'],
            'indicator': fact['dim']['GHO'],
            'value': fact['Value'],
            'year': fact['dim']['YEAR'],
        }

        yield record
