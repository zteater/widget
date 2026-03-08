from fastapi.testclient import TestClient

from widget.app import app, store

client = TestClient(app)


def setup_function() -> None:
    store.clear()


def test_widget_crud_flow() -> None:
    created = client.post(
        "/widgets",
        json={"name": "starter widget", "description": "first draft"},
    )

    assert created.status_code == 201
    widget = created.json()
    assert widget["name"] == "starter widget"
    assert widget["description"] == "first draft"

    listed = client.get("/widgets")
    assert listed.status_code == 200
    assert listed.json() == [widget]

    fetched = client.get(f"/widgets/{widget['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == widget

    updated = client.put(
        f"/widgets/{widget['id']}",
        json={"name": "renamed widget", "description": "updated draft"},
    )
    assert updated.status_code == 200
    updated_widget = updated.json()
    assert updated_widget["name"] == "renamed widget"
    assert updated_widget["description"] == "updated draft"
    assert updated_widget["updated_at"] != widget["updated_at"]

    deleted = client.delete(f"/widgets/{widget['id']}")
    assert deleted.status_code == 204
    assert deleted.content == b""

    missing = client.get(f"/widgets/{widget['id']}")
    assert missing.status_code == 404


def test_missing_widget_returns_404() -> None:
    response = client.get("/widgets/123e4567-e89b-12d3-a456-426614174000")

    assert response.status_code == 404
    assert response.json() == {"detail": "Widget not found"}
