from uuid import UUID
from pydantic import BaseModel


class MatchScore(BaseModel):
    uuid: UUID
    match_set_score_id: UUID
    score_team_id: UUID
    home_team_score: int
    away_team_score: int
    sequence_number: int
