import pytest
import pytest_no_fixtures.shared.api_methods as api


def create_organization(params={}):
    query_params = {
        "displayName": pytest.org_name
    }
    query_params.update(params)
    response = api.post(pytest.org_create_url, query_params)
    assert response.status_code == 200,\
        "Failure reason: {}. Failure desc: {}".format(response.reason, response.text)


def clear_organization_boards():
    url = pytest.org_by_id_url.replace("{id}", pytest.org_name)
    response = api.delete(url)
    assert response.status_code == 200 or response.status_code == 404, \
        "Failure reason: {}. Failure desc: {}".format(response.reason, response.text)
    # increment = 0
    # while True:
    #     increment = increment + 1
    #     url = pytest.org_by_id_url.replace("{id}", pytest.org_name + str(increment))
    #     response = api.delete(url)
    #     if response.status_code == 404:
    #         break
