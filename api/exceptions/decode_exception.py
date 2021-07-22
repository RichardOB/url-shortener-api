from http import HTTPStatus

class DecodeException(Exception):

    def __init__(self):
        """Initialise a DecodeException that will always have a status code of 404 and a 'No URL Found' message"""
        self.status_code = HTTPStatus.NOT_FOUND
        self.message = "No URL Found"