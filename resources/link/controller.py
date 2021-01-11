from flask_restful import Resource
from .service import short_link, link_redirection
from flask import request


class LinkShort(Resource):
    """
    Controller for link shorten
    """

    def put(self):
        user_data = request.get_json(force=True)
        new_link = short_link(user_data)
        return new_link


class LinkRedirection(Resource):
    """
        Controller for link redirection
    """

    def get(self, short_hash):
        return link_redirection(short_hash)
