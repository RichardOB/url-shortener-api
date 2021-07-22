from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import datetime

ma = Marshmallow()

class UrlShortenRequestSchema(ma.Schema):
    long_url = fields.String(required=True)

class UrlHashRequestSchema(ma.Schema):
    url_hash = fields.String(required=True)