import pytest
import requests

import pytest_no_fixtures.shared.organization_api as org_api
import pytest_no_fixtures.shared.board_api as board_api

wrong_token = {"key": pytest.auth["key"], "token": "Blahblahblah"}
wrong_key = {"token": pytest.auth["token"], "key": "Blahblahblah"}


@pytest.mark.parametrize("auth", [{}, wrong_token, wrong_key])
def test_create_board_without_auth(auth):
    org_api.clear_organization_boards()
    org_api.create_organization()

    query_params = {
        "name": "Board without ID",
        "organizationId": pytest.org_name
    }
    query_params.update(auth)
    response = requests.post(
        pytest.board_create_url, params=query_params
    )
    assert response.status_code == 401


@pytest.mark.parametrize("auth", [{}, wrong_token, wrong_key])
def test_get_board_without_auth(auth):
    org_api.clear_organization_boards()
    org_api.create_organization()

    board_id = board_api.create_board()["id"]
    url = pytest.board_by_id_url.replace("{id}", board_id)
    response = requests.get(
        url, params=auth
    )
    assert response.status_code == 401


def test_update_board_without_auth():
    org_api.clear_organization_boards()
    org_api.create_organization()

    board_id = board_api.create_board()["id"]
    url = pytest.board_by_id_url.replace("{id}", board_id)
    response = requests.put(
        url
    )
    assert response.status_code == 401


def test_update_board_with_wrong_token():
    org_api.clear_organization_boards()
    org_api.create_organization()

    board_id = board_api.create_board()["id"]
    url = pytest.board_by_id_url.replace("{id}", board_id)
    response = requests.put(
        url, params=wrong_token
    )
    assert response.status_code == 401


def test_update_board_with_wrong_kye():
    org_api.clear_organization_boards()
    org_api.create_organization()

    board_id = board_api.create_board()["id"]
    url = pytest.board_by_id_url.replace("{id}", board_id)
    response = requests.put(
        url, params=wrong_key
    )
    assert response.status_code == 401
