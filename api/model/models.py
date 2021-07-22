
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class ShortenedUrl(db.Model):
    __tablename__ = 'shortened_urls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    short_url = db.Column(db.String)
    url_usages = db.relationship("ShortenedUrlUsage", back_populates="shortened_url")
    created_at =  db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, url):
        self.url = url


class ShortenedUrlUsage(db.Model):
    __tablename__ = 'shortened_url_usages'

    id = db.Column(db.Integer, primary_key=True)
    shortened_url_id = db.Column(db.Integer, db.ForeignKey('shortened_urls.id'))
    shortened_url = db.relationship("ShortenedUrl", back_populates="url_usages")
    used_at =  db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, shortened_url):
        self.shortened_url = shortened_url