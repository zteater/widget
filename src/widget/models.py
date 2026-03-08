from datetime import UTC, datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


def utc_now() -> datetime:
    return datetime.now(UTC)


class WidgetBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)


class WidgetCreate(WidgetBase):
    pass


class WidgetUpdate(WidgetBase):
    pass


class Widget(WidgetBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
