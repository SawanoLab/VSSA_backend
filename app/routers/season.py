import cruds.season as crud_season
from database import get_db
from fastapi import APIRouter, Depends
from schemas.season import SeasonResponse, SeasonBase, SeasonCreate
from sqlalchemy.orm import Session
from typing import List

season_router = APIRouter()


@season_router.get('/', response_model=List[SeasonResponse])
async def get_seasons(user_id: str, db: Session = Depends(get_db)):
    items = await crud_season.get_seasons(db, user_id)
    return items


@season_router.post("/", response_model=SeasonResponse)
async def create_season(season: SeasonBase, db: Session = Depends(get_db)):
    item = await crud_season.create_season(db, season)
    return item


@ season_router.delete("/{season_id}", response_model=SeasonResponse)
async def delete_season(user_id: str, season_id: str, db: Session = Depends(get_db)):
    item = await crud_season.delete_seasons(db, user_id, season_id)
    return item


@season_router.put("/{season_id}", response_model=SeasonResponse)
async def update_season(user_id: str, season_id: str, season: SeasonCreate, db: Session = Depends(get_db)):
    item = await crud_season.update_season(db, user_id, season_id, season)
    return item
