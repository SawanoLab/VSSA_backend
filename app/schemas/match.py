from typing import Dict, Optional
from uuid import UUID
from pydantic import BaseModel


class PlayerInfo(BaseModel):
    uuid: str
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
    team_name: str
    players: Dict[str, TeamPlayers]
    setter_postion: str


class MatchRequest(BaseModel):
    home_team: TeamRequest
    away_team: TeamRequest
    season_name: str


class PlayerMatchInfo(BaseModel):
    player_id: str
    on_court: bool
    zone_code: Optional[str]
    libero: Optional[bool]


class Match(BaseModel):
    home_team_id: str
    away_team_id: str
    user_id: str
    season_id: str


class MatchPostRequest(BaseModel):
    Match: Match
    PlayerMatchInfo: Dict[str, PlayerMatchInfo]
