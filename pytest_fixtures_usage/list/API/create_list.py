import pytest_fixtures_usage.shared.list_api as list_api


def test_create_valid_list(create_list):
    name = "new_list"
    query_params = {
        "name": name
    }
    res = create_list(query_params)
    assert res["name"] == name, \
        "Created list don't have expected name: {}, but have: {} instead".format(name, res["name"])


def test_create_list_without_name(create_board):
    board_id = create_board()["id"]
    query_params = {
        "name": "",
        "idBoard": board_id
    }
    res = list_api.try_to_create_list(query_params)

    assert res.status_code == 400 and res.text == "invalid value for name",\
        "Expected \"invalid value for name\" but got status code: {} and context: {}".format(res.status_code, res.text)


def test_create_list_without_board_id():
    query_params = {
        "name": "list_name",
        "idBoard": ""
    }
    res = list_api.try_to_create_list(query_params)
    print(res)
    assert res.status_code == 400 and res.text == "invalid value for idBoard",\
        "Expected \"invalid value for name\" but got status code: {} and context: {}".format(res.status_code, res.text)


def test_crete_list_from_template(create_list):
    # може це на карточки розраховане
    t_name = "template_list"
    t_query_params = {
        "name": t_name
    }
    t_res = create_list(t_query_params)
    template_list_id = t_res["id"]

    name = "list_based_on_template"
    query_params = {
        "idListSource": template_list_id,
        "name": name
    }
    res = create_list(query_params)
    assert res["name"] == t_name, \
        "Created list don't have expected name: {}, but have: {} instead".format(name, res["name"])