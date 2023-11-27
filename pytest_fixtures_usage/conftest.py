from selenium.webdriver import Chrome
import pytest
from urllib.parse import urljoin

from pytest_fixtures_usage.api_fixtures import create_board, create_organization, clear_organization_boards, create_list

__all__ = [
    "create_board",
    "create_organization",
    "clear_organization_boards",
    "create_list"
]


def pytest_configure():
    pytest.org_name = "defaultorg"
    pytest.latest_board_id = ""
    pytest.auth = {
        "key": "1b7b5e70620dfa4b23208bc12a6c84c1",
        "token": "ATTA543c51049df436fa6792cd472760a365ca02219759c47426eb8e3441181b02eb712B9160"
    }
    pytest.BASE_URL = "https://api.trello.com"
    pytest.version = "1/"

    # board
    pytest.board_create_url = urljoin(pytest.BASE_URL, pytest.version + "boards")
    pytest.board_by_id_url = urljoin(pytest.BASE_URL, pytest.version + "boards/{id}")
    # organization
    pytest.org_create_url = urljoin(pytest.BASE_URL, pytest.version + "organizations")
    pytest.org_by_id_url = urljoin(pytest.BASE_URL, pytest.version + "organizations/{id}")
    # list
    pytest.list_create_url = urljoin(pytest.BASE_URL, pytest.version + "lists")
    pytest.get_list_from_board_url = urljoin(pytest.BASE_URL, pytest.version + "boards/{id}/lists")

@pytest.fixture
def driver():
    _driver = Chrome()
    yield _driver
    _driver.quit()

