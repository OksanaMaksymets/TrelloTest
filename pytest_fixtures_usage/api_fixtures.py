import json
import pytest
import random
import string

import pytest_fixtures_usage.shared.api_methods as api


@pytest.fixture(scope="session")
def create_organization(params={}):
    query_params = {
        "displayName": pytest.org_name
    }
    query_params.update(params)
    response = api.post(pytest.org_create_url, query_params)
    assert response.status_code == 200,\
        "Failure reason: {}. Failure desc: {}".format(response.reason, response.text)


@pytest.fixture(scope="function")
def create_board(create_organization):
    def _create_board(params={}):
        query_params = {
            "name": ''.join(random.choices(string.ascii_lowercase, k=5)),
            "organizationId": pytest.org_name
        }
        query_params.update(params)
        response = api.post(pytest.board_create_url, query_params)
        assert response.status_code == 200,\
            "Failure reason: {}. Failure desc: {}".format(response.reason, response.text)
        res = json.loads(response.text)

        pytest.latest_board_id = res["id"]
        return res
    return _create_board


@pytest.fixture(scope="session", autouse=True)
def clear_organization_boards():
    url = pytest.org_by_id_url.replace("{id}", pytest.org_name)
    response = api.delete(url)
    print(response)
    assert response.status_code == 200 or response.status_code == 404, \
        "Failure reason: {}. Failure desc: {}".format(response.reason, response.text)
    # increment = 0
    # while True:
    #     increment = increment + 1
    #     url = pytest.org_by_id_url.replace("{id}", pytest.org_name + str(increment))
    #     response = api.delete(url)
    #     if response.status_code == 404:
    #         break


@pytest.fixture(scope="function")
def create_list(create_board):
    def _create_list(params=None):
        board_id = create_board()["id"]
        query_params = {
            "name": "".join(random.choices(string.ascii_lowercase, k=5)),
            "idBoard": board_id
        }
        query_params.update(params)
        response = api.post(pytest.list_create_url, query_params)
        assert response.status_code == 200, \
            "Failure reason: {}. Failure desc: {}".format(response.reason, response.text)
        res = json.loads(response.text)

        pytest.latest_list_id = res["id"]
        return res

    return _create_list
