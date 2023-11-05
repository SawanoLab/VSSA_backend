from pydantic import BaseModel
from uuid import UUID


class TeamBase(BaseModel):
    name: str
    code: str
    director: str
    coach: str
    trainer: str
    doctor: str
    season_id: UUID
    user_id: UUID

    class Config:
        orm_mode = True

class TeamCreate(TeamBase):
    uuid: UUID

class TeamGet(TeamBase):
    uuid: UUID
