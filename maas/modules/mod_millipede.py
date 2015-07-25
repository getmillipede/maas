"""
Millipede calls
"""
# ok to deactivate it for flask
# pylint: disable=C0103,C0111,W0232,R0903

from millipede import millipede

from flask import Blueprint, make_response, g
from flask_restful import Api, Resource, reqparse

from lib.reqtypes import boolean


millipede_mod = Blueprint('millipede_mod', __name__)
millipede_api = Api(millipede_mod)


class Millipede(Resource):
    """
    Handle millipede calls
    """

    @staticmethod
    def get():
        """
        Return a millipede
        """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('size', default=20, type=int)
        parser.add_argument('reverse', type=boolean, default=False)
        parser.add_argument('comment', type=str, default=None)

        args = parser.parse_args()

        cached = None
        if g.redis:
            key = "{}#{}#{}".format(args.size,
                                    args.reverse,
                                    args.comment)
            cached = g.redis.get(key)

        if not cached:
            value = millipede(args.size, args.comment, args.reverse)
        else:
            value = cached

        response = make_response(value)
        response.headers['Content-type'] = 'text/plain; charset=utf-8'

        if g.redis and not cached:
            g.redis.set(key, value)

        return response


millipede_api.add_resource(Millipede, '/')
