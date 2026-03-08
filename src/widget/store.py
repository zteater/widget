from collections.abc import Iterable
from uuid import UUID

from widget.models import Widget, WidgetCreate, WidgetUpdate, utc_now


class WidgetStore:
    def __init__(self) -> None:
        self._widgets: dict[UUID, Widget] = {}

    def list(self) -> Iterable[Widget]:
        return sorted(self._widgets.values(), key=lambda widget: widget.created_at)

    def create(self, payload: WidgetCreate) -> Widget:
        widget = Widget(**payload.model_dump())
        self._widgets[widget.id] = widget
        return widget

    def get(self, widget_id: UUID) -> Widget | None:
        return self._widgets.get(widget_id)

    def update(self, widget_id: UUID, payload: WidgetUpdate) -> Widget | None:
        existing = self.get(widget_id)
        if existing is None:
            return None

        updated = existing.model_copy(
            update={**payload.model_dump(), "updated_at": utc_now()},
        )
        self._widgets[widget_id] = updated
        return updated

    def delete(self, widget_id: UUID) -> Widget | None:
        return self._widgets.pop(widget_id, None)

    def clear(self) -> None:
        self._widgets.clear()
