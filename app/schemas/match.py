from typing import Dict, Optional
from uuid import UUID
from pydantic import BaseModel


class PlayerInfo(BaseModel):
    uuid: UUID
    name: str
    player_number: int
    code: str
    postion: str
    weight: Optional[int]
    height: Optional[int]


class TeamPlayers(BaseModel):
    PlayerInfo: PlayerInfo
    onCourt: bool
    zone_code: Optional[str]
    libero: Optional[bool]


class TeamRequest(BaseModel):
    uuid: UUID
    team_name: str
    players: Dict[str, TeamPlayers]
    setter_postion: str


class MatchRequest(BaseModel):
    uuid: UUID
    home_team: TeamRequest
    away_team: TeamRequest
    season_name: str
    # home_team_score: int
    # away_team_score: int


class PlayerMatchInfo(BaseModel):
    player_id: UUID
    on_court: bool
    zone_code: Optional[str]
    libero: Optional[bool]


class Match(BaseModel):
    home_team_id: UUID
    away_team_id: UUID
    user_id: UUID
    season_id: UUID


class MatchPostRequest(BaseModel):
    Match: Match
    PlayerMatchInfo: Dict[str, PlayerMatchInfo]
