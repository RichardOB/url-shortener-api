import jwt
import datetime
import sqlalchemy

from http import HTTPStatus
from flask import request, jsonify, make_response
from flask.blueprints import Blueprint
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from api.model.models import db
from api.daos import shortened_url_dao, shortened_url_usage_dao
from api.helpers import integer_encoder, url_validator
from api.schema.schemas import UrlShortenRequestSchema
from api.exceptions.decode_exception import DecodeException


url_shortener_api = Blueprint('url_shortener', __name__)

url_shorten_request_schema = UrlShortenRequestSchema()

@url_shortener_api.route('/', methods=['POST'])
def create_short_url():
    #1. Get URL from request. Throw exception if none provided.
    json_data = request.json

    if not json_data:
        return {
            'message': 'No input data provided'
        }, 400
    
    try:
        data = url_shorten_request_schema.load(json_data)

        long_url = data['long_url']

        #2. Check if URL Valid. Throw excdption if not.
        url_validator.validate_url(long_url)
        #3. Create shortened_url object without short_url.
        shortened_url = shortened_url_dao.create(long_url)
        #4. Flush DB to get id of shortened url
        db.session.flush()
        url_id = shortened_url.id
        #5. Use ID To generate hash
        url_hash = integer_encoder.encode_number(url_id)
        #6. Add hash to shortened_url object
        shortened_url.short_url = url_hash
        #7. Commit to db
        db.session.commit()
        #8. Return hash as Json response (201 created)
        return {
            "status": 'success', 
            'url_hash': url_hash 
        }, HTTPStatus.CREATED

    except ValidationError as exc:
        return {
            'message': "Validation errors", 
            'errors': exc.messages
        }, HTTPStatus.BAD_REQUEST
    except Exception as exc:
        print(exc)
        return {
            'message': "Unexpected error",
        }, HTTPStatus.BAD_REQUEST
    

@url_shortener_api.route('/<url_hash>', methods=['GET'])
def get_short_url_redirect(url_hash):
    #1. Get URL Hash from request. Throw exception if none provided.
    try:
        #2. Attempt to decode hash. Throw exception if cant.
        decoded_url_hash = integer_encoder.decode_hash(url_hash)
        #3. Use decoded hash (id of url) to fetch Shortened Url Object from DB (Throw exception if not found)
        shortened_url = shortened_url_dao.fetch(decoded_url_hash)
        #4. Create new ShortenedUrlUsage object and add to Shortened Url.
        url_usage = shortened_url_usage_dao.create(shortened_url)
        #5. Commit to db
        db.session.commit()
        #6. Return original url as Json response.
        return {
            "status": 'success', 
            'url': shortened_url.url 
        }, HTTPStatus.OK

    except TypeError:
        return {
            'message': "Missing required positional argument for url_hash",
        }, HTTPStatus.BAD_REQUEST
    except DecodeException as exc:
        return {
            'message': exc.message,
        }, exc.status_code
    except NoResultFound:
        return {
            'message': "No URL Found",
        }, HTTPStatus.NOT_FOUND