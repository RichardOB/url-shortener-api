import jwt
import datetime
import sqlalchemy

from http import HTTPStatus
from flask import request, jsonify, make_response, redirect
from flask.blueprints import Blueprint
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from api.model.models import db
from api.daos import shortened_url_dao, shortened_url_usage_dao
from api.helpers import integer_encoder, url_validator
from api.schema.schemas import UrlShortenRequestSchema
from api.exceptions.decode_exception import DecodeException


url_statistics_api = Blueprint('url_statistics', __name__)

url_shorten_request_schema = UrlShortenRequestSchema()
    

@url_statistics_api.route('/<url_hash>', methods=['GET'])
def get_short_url_redirect(url_hash):
    #Get URL Hash from request. Throw exception if none provided.
    try:
        #Attempt to decode hash. Throw exception if cant.
        decoded_url_hash = integer_encoder.decode_hash(url_hash)
        #Use decoded hash (id of url) to fetch Shortened Url Object from DB (Throw exception if not found)
        shortened_url = shortened_url_dao.fetch(decoded_url_hash)
        #Get ShortenedUrlUsage count.
        url_usage_count = shortened_url_usage_dao.get_total_usage_count_for_short_url(shortened_url)
        last_visit = shortened_url_usage_dao.get_last_visit_for_url(shortened_url)
        #Return statistics.
        return {
            'status': 'success',
            'long_url': shortened_url.url,
            'usage_count': url_usage_count,
            'last_visit': last_visit.used_at if last_visit is not None else None
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