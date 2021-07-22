import uuid
from api.model.models import db, ShortenedUrl

def create(url):
    shortened_url = ShortenedUrl(url=url)
    db.session.add(shortened_url)
    return shortened_url

def fetch(id):
    return db.session.query(ShortenedUrl).filter_by(id=id).one()
