from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from uuid import uuid4

from models.match import Match
from models.matchScore import MatchScore
from models.playerMatchInfo import PlayerMatchInfo
from schemas.match import MatchRequest, TeamRequest, TeamPlayers, \
    MatchPostRequest


def create_team_player(info: PlayerMatchInfo):
    return TeamPlayers(
        PlayerInfo={**info.player.__dict__},
        onCourt=info.on_court,
        zone_code=info.zone_code,
        libero=info.libero
    )


def create_team_request(team_name: str,
                        team_players: list,
                        setter_postion: str):
    return TeamRequest(
        team_name=team_name,
        players={str(player.PlayerInfo.uuid):
                 player for player in team_players},
        setter_postion=setter_postion
    )


def init_match_score() -> MatchScore:
    return MatchScore(
        uuid=uuid4(),
        # home_team_score=0,
        # away_team_score=0
    )


def create_team_players(team, player_match_info):
    return [create_team_player(info)
            for info in player_match_info
            if info.player.team_id == team.uuid]


def assemble_match_request(match: Match):
    home_team_players = create_team_players(
        match.home_team, match.player_match_info)
    away_team_players = create_team_players(
        match.away_team, match.player_match_info)
    home_team_request = create_team_request(
        match.home_team.name, home_team_players, "Z1")
    away_team_request = create_team_request(
        match.away_team.name, away_team_players, "Z1")

    return MatchRequest(
        uuid=str(match.uuid),
        home_team=home_team_request,
        away_team=away_team_request,
        season_name=match.season.season_name,
    )


def get_matches(db: Session, user_id: str, skip: int = 0, limit: int = 100):
    try:
        items = db.query(Match).filter(
            Match.user_id == user_id).offset(skip).limit(limit).all()
        return [assemble_match_request(match) for match in items]
    except Exception as e:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(e))


def get_match(db: Session, user_id: str, match_id: str) -> MatchRequest:
    try:
        match = db.query(Match).filter(
            Match.uuid == match_id and Match.user_id == user_id).first()
        return assemble_match_request(match)
    except Exception as e:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(e))


def create_match(db: Session, matchPostRequest: MatchPostRequest) -> MatchPostRequest:
    try:
        match_score_item = init_match_score()
        db.add(match_score_item)
        match_item = Match(
            **matchPostRequest.Match.__dict__,
            uuid=uuid4(),
            matchscore_id=match_score_item.uuid
        )
        db.add(match_item)
        db.commit()
        db.refresh(match_item)
        for _, player_info in matchPostRequest.PlayerMatchInfo.items():
            item = PlayerMatchInfo(uuid=uuid4(),
                                   match_id=match_item.uuid,
                                   **player_info.__dict__)
            db.add(item)
        db.commit()
        db.refresh(match_item)
        db.refresh(match_score_item)
        return matchPostRequest
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(e))
