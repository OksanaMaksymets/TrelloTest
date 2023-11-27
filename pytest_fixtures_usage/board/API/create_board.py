import pytest_fixtures_usage.shared.board_api as board_api


def test_create_valid_board(create_board):
    board_name = "Test Board"
    params = {"name": board_name}

    board_id = create_board(params)["id"]
    returned_board_name = board_api.get_board_by_id(board_id)["name"]

    assert board_name == returned_board_name, \
        "Create board with '{}', but returned with '{}'".format(board_name, returned_board_name)


def test_create_board_with_background_color(create_board):
    background_rgb = "#4BBF6B"
    background_color = "lime"
    query_params = {
        "prefs_background": background_color
    }

    res = create_board(query_params)
    board_id = res['id']
    preferences = board_api.get_board_by_id(board_id)["prefs"]

    assert preferences["backgroundColor"] == background_rgb and preferences["background"] == background_color


def test_create_board_from_source(create_board):
    query_params = {
        "defaultLists": "false"
    }
    source_board_id = create_board(query_params)["id"]
    query_params = {
        "defaultLists": "true",
        "idBoardSource": source_board_id
    }
    board_id = create_board(query_params)["id"]
    returned_list = board_api.get_list_from_board_by_id(board_id)
    assert not returned_list, "Board list are not empty, it has {} elements".format(len(returned_list))


def test_create_board_without_name():
    query_params = {
        "name": ""
    }
    res = board_api.try_to_create_board(query_params)
    print(res)
    assert res.status_code == 400 and res.text == "invalid value for name", \
        "Failure reason: {}. Failure desc: {}".format(res.reason, res.text)

def test_default_values_replacing_invalid_fields():
    pass