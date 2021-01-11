from flask_restful import Resource
from .service import short_link, link_redirection
from flask import request


class LinkShort(Resource):
    def put(self):
        user_data = request.get_json(force=True)
        user_link = user_data['link']
        new_link = short_link(user_link)
        return new_link


class LinkRedirection(Resource):
    def get(self, short_hash):
        return link_redirection(short_hash)
