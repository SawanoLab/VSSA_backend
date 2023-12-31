from pydantic import BaseModel
from uuid import UUID


class PlayerBase(BaseModel):
    name: str
    player_number: int
    code: str
    postion: str
    weight: int
    height: int
    user_id: UUID
    team_id: UUID
    season_id: UUID

    class Config:
        orm_mode = True


class PlayerCreate(PlayerBase):
    uuid: UUID


class PlayerGet(PlayerBase):
    uuid: UUID


class PlayerDelete(PlayerBase):
    uuid: UUID


class PlayerUpdate(PlayerBase):
    uuid: UUID


class PlayerResponse(PlayerBase):
    uuid: UUID
