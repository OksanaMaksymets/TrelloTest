import json
import pytest
import random
import string

import pytest_fixtures_usage.shared.api_methods as api


def try_to_create_list(params):
    query_params = {
        'name': 'default_list_name'
    }
    query_params.update(params)
    response = api.post(pytest.list_create_url, params)
    return response
