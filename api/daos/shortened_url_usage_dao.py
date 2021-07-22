import uuid
from api.model.models import db, ShortenedUrl, ShortenedUrlUsage
from sqlalchemy import func

def create(shortened_url:ShortenedUrl):
    shortened_url_usage = ShortenedUrlUsage(shortened_url=shortened_url)
    db.session.add(shortened_url_usage)
    return shortened_url_usage

def get_total_usage_count_for_short_url(shortened_url):
    return db.session.query(ShortenedUrlUsage.id).filter_by(shortened_url=shortened_url).count()

def get_last_visit_for_url(shortened_url):
    return db.session.query(ShortenedUrlUsage).filter_by(shortened_url=shortened_url).order_by(ShortenedUrlUsage.used_at.desc()).first()