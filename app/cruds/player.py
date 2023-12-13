from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
from typing import List
from uuid import uuid4
from models.player import Player
from schemas.player import PlayerBase, PlayerGet
from utils.logger import get_logger


async def get_players(db: Session, user_id: str) -> List[PlayerGet]:
    try:
        items = db.query(Player).filter(Player.user_id == user_id).all()
        players = [PlayerGet.from_orm(item) for item in items]
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='No players found')
    return players


def create_player(db: Session, player: PlayerBase) -> PlayerBase:
    try:
        db_player = Player(**player.dict(), uuid=uuid4())
        db.add(db_player)
        db.commit()
        db.refresh(db_player)
    except Exception:
        get_logger().error('Player not created')
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Player not created')
    return PlayerBase.from_orm(db_player)


def delete_player(db: Session, user_id: str, player_id: str) -> PlayerBase:
    try:
        db_player = db.query(Player).filter(Player.user_id == user_id,
                                            Player.uuid == player_id).first()
        db.delete(db_player)
        db.commit()
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Player not deleted')
    return []


def update_player(db: Session,
                  user_id: str,
                  player_id: str,
                  player: PlayerBase
                  ) -> PlayerBase:
    try:
        db_player = db.query(Player).filter(Player.user_id == user_id,
                                            Player.uuid == player_id).first()
        db_player.name = player.name
        db_player.player_number = player.player_number
        db_player.code = player.code
        db_player.postion = player.postion
        db_player.weight = player.weight
        db_player.height = player.height
        db_player.user_id = player.user_id
        db_player.team_id = player.team_id
        db_player.season_id = player.season_id
        db.commit()
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Player not updated')
    return PlayerBase.from_orm(db_player)
