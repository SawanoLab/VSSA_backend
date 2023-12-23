from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class SeasonBase(BaseModel):
    start_day: datetime
    end_day: datetime
    season_name: str
    game_format: str
    code: str
    user_id: UUID

    class Config:
        orm_mode = True


class SeasonCreate(SeasonBase):
    uuid: UUID


class SeasonResponse(SeasonBase):
    uuid: UUID
