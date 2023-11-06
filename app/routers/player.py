from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.player import PlayerGet, PlayerBase
from database import get_db
from typing import List
import cruds.player as crud_team


player_router = APIRouter()


@player_router.get('/', response_model=List[PlayerGet])
async def get_players(user_id: str, db: Session = Depends(get_db)):
    items = crud_team.get_players(db, user_id)
    return items

@player_router.post('/', response_model=PlayerBase)
async def create_player(player: PlayerBase, db: Session = Depends(get_db)):
    item = crud_team.create_player(db, player)
    return item
