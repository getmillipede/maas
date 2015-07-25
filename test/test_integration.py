"""
Integration tests for Millipede as a Service
"""
# -*- coding: utf-8 -*-

import requests
from millipede import millipede

API_VERSION = '0.0.1'
API_PORT = '3000'
URL = 'http://localhost:{}/api/{}'.format(API_PORT, API_VERSION)

def test_simple_millipede():
    """
    Test a simple millipede
    """
    url = "{}/millipede/".format(URL)
    response = requests.get(url)

    assert response.text.encode('utf-8') == millipede(20)

def test_millipede_30():
    """
    Test a size 30 millipede
    """
    url = "{}/millipede/".format(URL)
    params = {
        'size': 30
    }
    response = requests.get(url, params=params)

    assert response.text.encode('utf-8') == millipede(**params)

def test_millipede_comment():
    """
    Test a millipede with a comment
    """
    url = "{}/millipede/".format(URL)
    params = {
        'size': 20,
        'comment': "Choo-choo my millipede is wunderbar!"
    }
    response = requests.get(url, params=params)

    assert response.text.encode('utf-8') == millipede(**params)

def test_millipede_reverse():
    """
    Test a reversed millipede
    """
    url = "{}/millipede/".format(URL)
    params = {
        'size': 20,
        'reverse': True,
    }
    response = requests.get(url, params=params)

    assert response.text.encode('utf-8') == millipede(**params)
