from flask_restful import Resource, abort, reqparse
from .service import save_new_link, db
from flask import request, json


class ShortLink(Resource):
    def get(self):
        return {(self.__class__.__name__): 'lol'}

    def put(self):
        user_data = request.get_json(force=True)
        user_link = user_data['Link']
        print(user_link)
        print(type(user_data['Link']))
        short_link = save_new_link(user_link)
        return short_link
