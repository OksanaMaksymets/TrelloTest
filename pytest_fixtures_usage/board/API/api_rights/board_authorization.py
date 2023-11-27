import pytest
import requests

wrong_token = {"key": pytest.auth["key"], "token": "Blahblahblah"}
wrong_key = {"token": pytest.auth["token"], "key": "Blahblahblah"}


@pytest.mark.parametrize("auth", [{}, wrong_token, wrong_key])
def test_create_board_without_auth(auth):
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
def test_get_board_without_auth(create_board, auth):
    board_id = create_board()["id"]
    url = pytest.board_by_id_url.replace("{id}", board_id)
    response = requests.get(
        url, params=auth
    )
    assert response.status_code == 401


@pytest.mark.parametrize("auth", [{}, wrong_token, wrong_key])
def test_update_board_without_auth(create_board, auth):
    board_id = create_board()["id"]
    url = pytest.board_by_id_url.replace("{id}", board_id)
    response = requests.put(
        url, params=auth
    )
    assert response.status_code == 401
