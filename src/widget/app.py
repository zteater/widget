from uuid import UUID

from fastapi import FastAPI, HTTPException, Response, status

from widget.models import Widget, WidgetCreate, WidgetUpdate
from widget.store import WidgetStore

app = FastAPI(title="widget", version="0.1.0")
store = WidgetStore()


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/widgets", response_model=list[Widget])
def list_widgets() -> list[Widget]:
    return list(store.list())


@app.post("/widgets", response_model=Widget, status_code=status.HTTP_201_CREATED)
def create_widget(payload: WidgetCreate) -> Widget:
    return store.create(payload)


@app.get("/widgets/{widget_id}", response_model=Widget)
def get_widget(widget_id: UUID) -> Widget:
    widget = store.get(widget_id)
    if widget is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Widget not found")
    return widget


@app.put("/widgets/{widget_id}", response_model=Widget)
def update_widget(widget_id: UUID, payload: WidgetUpdate) -> Widget:
    widget = store.update(widget_id, payload)
    if widget is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Widget not found")
    return widget


@app.delete("/widgets/{widget_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_widget(widget_id: UUID) -> Response:
    deleted = store.delete(widget_id)
    if deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Widget not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
