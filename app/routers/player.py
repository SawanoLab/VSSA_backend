from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.player import PlayerResponse, PlayerBase
from database import get_db
from typing import List
import cruds.player as crud_team


player_router = APIRouter()


@player_router.get('/', response_model=List[PlayerResponse])
async def get_players(user_id: str, db: Session = Depends(get_db)):
    items = await crud_team.get_players(db, user_id)
    return items


@player_router.post('/', response_model=PlayerResponse)
async def create_player(player: PlayerBase, db: Session = Depends(get_db)):
    item = await crud_team.create_player(db, player)
    return item


@player_router.delete('/{player_id}', response_model=PlayerResponse)
async def delete_player(user_id: str,
                        player_id: str,
                        db: Session = Depends(get_db)):
    item = await crud_team.delete_player(db, user_id, player_id)
    return item


@player_router.put('/{player_id}', response_model=PlayerResponse)
async def update_player(user_id: str,
                        player_id: str,
                        player: PlayerBase,
                        db: Session = Depends(get_db)):
    item = await crud_team.update_player(db, user_id, player_id, player)
    return item
