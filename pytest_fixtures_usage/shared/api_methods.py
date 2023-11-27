import pytest
import requests


def get(url):
    se = requests.Session()
    response = se.get(
        url, params=pytest.auth
    )
    return response


def post(url, params):
    params.update(pytest.auth)
    se = requests.Session()
    response = se.post(
        url, params=params
    )
    return response


def delete(url):
    se = requests.Session()
    response = se.delete(
        url,
        params=pytest.auth
    )
    return response


def update(url, params):
    params.put(pytest.auth)
    se = requests.Session()
    response = se.post(
        url, params=params
    )
    return response
