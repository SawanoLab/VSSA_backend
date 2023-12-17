import cruds.season as crud_season
from database import get_db
from fastapi import APIRouter, Depends
from schemas.season import SeasonGet, SeasonBase
from sqlalchemy.orm import Session
from typing import List

season_router = APIRouter()


@season_router.get('/', response_model=List[SeasonGet])
async def get_seasons(user_id: str,
                      db: Session = Depends(get_db)):
    items = await crud_season.get_seasons(db, user_id)
    return items


@season_router.post("/", response_model=SeasonBase)
async def create_season(season: SeasonBase, db: Session = Depends(get_db)):
    print('season: ', season)
    item = await crud_season.create_season(db, season)
    return item
