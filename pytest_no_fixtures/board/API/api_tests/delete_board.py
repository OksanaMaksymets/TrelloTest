import pytest_no_fixtures.shared.organization_api as org_api
import pytest_no_fixtures.shared.board_api as board_api


def test_delete_board(create_board):
    org_api.clear_organization_boards()
    org_api.create_organization()

    board_id = create_board()["id"]

    board_api.delete_board_by_id(board_id)
    res = board_api.try_to_get_board_by_id(board_id)

    assert res.status_code == 404, "Failure reason: {}. Failure desc: {}".format(res.reason, res.text)
