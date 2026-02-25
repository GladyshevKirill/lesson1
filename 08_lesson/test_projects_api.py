import time
import uuid

import pytest

from yougile_client import YougileClient

BASE_URL = "https://ru.yougile.com"
TOKEN = "ТОКЕН"  # ВСТАВЬТЕ ТОКЕН СЮДА


def unique_title(prefix: str) -> str:
    return f"{prefix}-{int(time.time())}-{uuid.uuid4().hex[:6]}"


@pytest.fixture()
def client() -> YougileClient:
    return YougileClient(BASE_URL, TOKEN)


@pytest.fixture()
def project_id(client: YougileClient) -> str:
    resp = client.create_project(unique_title("project"))
    assert resp.status_code in (200, 201), resp.text
    return resp.json()["id"]


def test_create_project_positive(client: YougileClient) -> None:
    resp = client.create_project(unique_title("create"))
    assert resp.status_code in (200, 201), resp.text
    assert resp.json().get("id")


def test_create_project_negative_empty_title(client: YougileClient) -> None:
    resp = client.create_project("")
    assert resp.status_code in (400, 401, 403, 422), resp.text


def test_get_project_positive(client: YougileClient, project_id: str) -> None:
    resp = client.get_project(project_id)
    assert resp.status_code == 200, resp.text
    assert resp.json().get("id") == project_id


def test_get_project_negative_not_found(client: YougileClient) -> None:
    resp = client.get_project("no_such_project_id")
    assert resp.status_code in (400, 404), resp.text


def test_update_project_positive(
        client: YougileClient, project_id: str
        ) -> None:
    new_title = unique_title("updated")
    resp = client.update_project(project_id, new_title)
    assert resp.status_code in (200, 204), resp.text

    check = client.get_project(project_id)
    assert check.status_code == 200, check.text
    assert check.json().get("title") == new_title


def test_update_project_negative_not_found(client: YougileClient) -> None:
    resp = client.update_project("no_such_project_id", unique_title("x"))
    assert resp.status_code in (400, 404), resp.text
