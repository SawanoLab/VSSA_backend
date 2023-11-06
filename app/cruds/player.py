from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
from typing import List
from uuid import uuid4
from uuid import UUID
from models.player import Player
from schemas.player import PlayerBase, PlayerGet


def get_players(db: Player, user_id: UUID) -> List[PlayerGet]:
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
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Player not created')
    return PlayerBase.from_orm(db_player)
