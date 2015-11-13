# -*- coding: utf-8 -*-
"""
    app.models
    ~~~~~~~~~~

    Provides the SQLAlchemy models
"""
from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

from datetime import datetime as dt
from app import db


class BaseMixin(object):
    # auto keys
    id = db.Column(db.Integer, primary_key=True)
    utc_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow())
    utc_updated = db.Column(
        db.DateTime, nullable=False, default=dt.utcnow(), onupdate=dt.utcnow())

    # other keys
    region = db.Column(db.String(64), nullable=False)
    indicator = db.Column(db.String(128), nullable=False)
    value = db.Column(db.Numeric, nullable=False)
    year = db.Column(db.Integer, nullable=False)
