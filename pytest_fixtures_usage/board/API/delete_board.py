import pytest_fixtures_usage.shared.board_api as board_api


def test_delete_board(create_board):
    board_id = create_board()["id"]

    board_api.delete_board_by_id(board_id)
    res = board_api.try_to_get_board_by_id(board_id)

    assert res.status_code == 404, "Failure reason: {}. Failure desc: {}".format(res.reason, res.text)
