from uuid import UUID
from pydantic import BaseModel


class MatchSetScore(BaseModel):
    uuid: UUID
    match_id: UUID
    set_number: int
    score_team_home: int
    score_team_away: int
