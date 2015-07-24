#!/usr/bin/env python
"""
MaaS: Millipede as a Service
"""

from flask import Flask

from modules.mod_millipede import millipede_mod


API_VERSION = '0.0.1'

app = Flask(__name__)
app.config['API_PREFIX'] = '/api'
app.config['API_VERSION'] = API_VERSION

def make_module_prefix(mod_name):
    """
    Generate the API path for route subscription
    """
    return '{}/{}/{}'.format(app.config['API_PREFIX'],
                             app.config['API_VERSION'],
                             mod_name)


app.register_blueprint(millipede_mod,
                       url_prefix=make_module_prefix('millipede'))


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
