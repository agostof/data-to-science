from uuid import UUID

from pydantic import BaseModel


# shared properties
class TeamBase(BaseModel):
    title: str | None = None
    description: str | None = None


# properties to receive via API on creation
class TeamCreate(TeamBase):
    title: str


# properties to receive via API on update
class TeamUpdate(TeamBase):
    pass


# properties shared by models stored in DB
class TeamInDBBase(TeamBase):
    id: UUID
    title: str

    class Config:
        orm_mode = True


# additional properties to return via API
class Team(TeamInDBBase):
    is_owner: bool = False


# additional properties stored in DB
class TeamInDB(TeamInDBBase):
    owner_id: UUID