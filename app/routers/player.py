from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.player import PlayerGet, PlayerBase, PlayerUpdate
from database import get_db
from typing import List
import cruds.player as crud_team


player_router = APIRouter()


@player_router.get('/', response_model=List[PlayerGet])
async def get_players(user_id: str, db: Session = Depends(get_db)):
    items = await crud_team.get_players(db, user_id)
    return items


@player_router.post('/', response_model=PlayerBase)
async def create_player(player: PlayerBase, db: Session = Depends(get_db)):
    item = crud_team.create_player(db, player)
    return item


@player_router.delete('/', response_model=PlayerBase)
async def delete_player(user_id: str,
                        player_id: str,
                        db: Session = Depends(get_db)):
    item = crud_team.delete_player(db, user_id, player_id)
    return item


@player_router.put('/', response_model=PlayerBase)
async def update_player(user_id: str,
                        player_id: str,
                        player: PlayerUpdate,
                        db: Session = Depends(get_db)):
    item = crud_team.update_player(db, user_id, player_id, player)
    return item
