from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from uuid import uuid4

from models.match import Match
from models.season import Season
from models.playerMatchInfo import PlayerMatchInfo
from schemas.match import MatchRequest, TeamRequest, TeamPlayers, MatchPostRequest


def get_matches(db: Session, user_id: str, skip: int = 0, limit: int = 100):
    try:
        # TODO: あとで修正
        # user_idを-を削除してから検索する
        user_id = user_id.replace("-", "")
        items = db.query(Match).filter(
            Match.user_id == user_id).offset(skip).limit(limit).all()
        match_requests = []
        for match in items:
            match_requests.append(get_match(db, match.uuid))
        return match_requests
    except Exception as e:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(e))


def get_match(db: Session, match_id: str) -> MatchRequest:
    match = db.query(Match).filter(Match.uuid == match_id).first()
    home_team_of_match = match.home_team
    away_team_of_match = match.away_team
    home_team_of_match_uuid = home_team_of_match.uuid
    away_team_of_match_uuid = away_team_of_match.uuid
    match_player_infos = match.player_match_info

    home_team_players = []
    away_team_players = []
    for info in match_player_infos:
        player = info.player
        team_players = TeamPlayers(
            PlayerInfo={
                "uuid": str(player.uuid),
                "name": player.name,
                "player_number": player.player_number,
                "code": player.code,
                "postion": player.postion,
                "weight": player.weight,
                "height": player.height,
            },
            onCourt=info.on_court,
            zone_code=info.zone_code,
            libero=info.libero
        )
        if player.team_id == home_team_of_match_uuid:
            home_team_players.append(team_players)
        elif player.team_id == away_team_of_match_uuid:
            away_team_players.append(team_players)

    home_team_request = TeamRequest(
        team_name=home_team_of_match.name,
        players={str(player.PlayerInfo.uuid):
                 player for player in home_team_players},
        setter_postion="Z2"
    )

    away_team_request = TeamRequest(
        team_name=away_team_of_match.name,
        players={str(player.PlayerInfo.uuid):
                 player for player in away_team_players},
        setter_postion="Z1"
    )

    item = MatchRequest(
        home_team=home_team_request,
        away_team=away_team_request,
        season_name=match.season.season_name
    )
    return item


def create_match(db: Session, match: MatchPostRequest) -> MatchPostRequest:
    try:
        match_uuid = uuid4()
        match_item = Match(
            uuid=match_uuid,
            home_team_id=match.Match.home_team_id.replace("-", ""),
            away_team_id=match.Match.away_team_id.replace("-", ""),
            user_id=match.Match.user_id.replace("-", ""),
            season_id=match.Match.season_id.replace("-", ""),
        )
        db.add(match_item)
        for key, player_info in match.PlayerMatchInfo.items():
            playerMatchInfo_item = PlayerMatchInfo(
                uuid=uuid4(),
                player_id=player_info.player_id.replace("-", ""),
                match_id=str(match_item.uuid).replace("-", ""),
                on_court=player_info.on_court,
                zone_code=player_info.zone_code,
                libero=player_info.libero
            )
            db.add(playerMatchInfo_item)
        print(db)
        db.commit()
        db.refresh(match_item)
        return match
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(e))
