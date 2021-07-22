import validators
from marshmallow import ValidationError

def validate_url(url):
    url_valid = validators.url(url)

    if not url_valid:
        raise ValidationError('Incorrect URL Format')
