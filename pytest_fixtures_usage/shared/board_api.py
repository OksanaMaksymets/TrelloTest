import json
import pytest
import random
import string

import pytest_fixtures_usage.shared.api_methods as api


def get_board_by_id(board_id):
    url = pytest.board_by_id_url.replace("{id}", board_id)
    response = api.get(url)
    assert response.status_code == 200, \
        "Failure reason: '{}'. Failure desc: '{}'".format(response.reason, response.text)
    return json.loads(response.text)


def get_list_from_board_by_id(board_id):
    url = pytest.get_list_from_board_url.replace("{id}", board_id)
    response = api.get(url)
    assert response.status_code == 200, \
        "Failure reason: '{}'. Failure desc: '{}'".format(response.reason, response.text)
    return json.loads(response.text)


def delete_board_by_id(board_id):
    url = pytest.board_by_id_url.replace("{id}", board_id)
    response = api.delete(url)
    assert response.status_code == 200, \
        "Failure reason: '{}'. Failure desc: '{}'".format(response.reason, response.text)


def update_board_by_id(board_id, params):
    url = pytest.board_by_id_url.replace("{id}", board_id)
    query_params = {
        "name": ''.join(random.choices(string.ascii_lowercase, k=5)),
        "organizationId": pytest.org_name
    }
    query_params.update(params)
    response = api.update(url, params)
    assert response.status_code == 200, \
        "Failure reason: '{}'. Failure desc: '{}'".format(response.reason, response.text)


def try_to_get_board_by_id(board_id):
    url = pytest.board_by_id_url.replace("{id}", board_id)
    response = api.get(url)
    return response


def try_to_create_board(params):
    query_params = {
        "organizationId": pytest.org_name
    }
    query_params.update(params)
    response = api.post(pytest.board_create_url, params)
    return response
