import uuid
from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from .flight import Flight
    from .group import Group
    from .user import User


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(300))
    location: Mapped[dict] = mapped_column(JSONB, nullable=False)
    planting_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    harvest_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    group_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("groups.id"), nullable=True)

    owner: Mapped["User"] = relationship(back_populates="projects")
    group: Mapped["Group"] = relationship(back_populates="projects")

    flights: Mapped[list["Flight"]] = relationship(back_populates="project", cascade="all, delete")

    def __repr__(self) -> str:
        return f"Project(id={self.id!r}, title={self.title!r}, description={self.description!r}, location={self.location!r}, planting_date={self.planting_date!r}, harvest_date={self.harvest_date!r}, owner_id={self.owner_id!r}, group_id={self.group_id!r})"