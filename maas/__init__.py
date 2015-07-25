#!/usr/bin/env python
"""
MaaS: Millipede as a Service
"""
# ok to deactivate it for flask
# pylint: disable=C0103

import sys
import os.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from os import environ

from redis import ConnectionError

from flask import Flask, g
from flask.ext.redis import FlaskRedis

from modules.mod_millipede import millipede_mod


API_VERSION = '0.0.1'
CONFIG_PATH = os.environ.get('MAAS_CONFIG_FILE', '/etc/maas.cfg')

app = Flask(__name__)
app.config['API_PREFIX'] = '/api'
app.config['API_VERSION'] = API_VERSION

if os.path.isfile(CONFIG_PATH):
    app.config.from_pyfile(CONFIG_PATH)

def make_module_prefix(mod_name):
    """
    Generate the API path for route subscription
    """
    return '{}/{}/{}'.format(app.config['API_PREFIX'],
                             app.config['API_VERSION'],
                             mod_name)


app.register_blueprint(millipede_mod,
                       url_prefix=make_module_prefix('millipede'))


@app.before_request
def before_request():
    """
    Setup before request
    """
    if not getattr(g, 'redis', None):
        redis_store = FlaskRedis(app)
        try:
            redis_store.client_list()
        except ConnectionError:
            redis_store = None
        g.redis = redis_store


@app.route('/')
def index():
    """
    Default page
    """
    return "Follow the white rabbit."


def main():
    """
    Development entry point
    """
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('host', nargs='?',
                        help="Give host",
                        default="0.0.0.0")
    parser.add_argument('-p', dest='port',
                        type=int, help="Give port", default=5000)
    args = parser.parse_args()

    app.run(debug=True, host=args.host, port=args.port)


if __name__ == '__main__':
    main()
