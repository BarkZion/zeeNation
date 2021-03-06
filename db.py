import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_type=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.get_db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()