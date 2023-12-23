from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
from typing import List
from uuid import uuid4
from uuid import UUID
from models.season import Season
from schemas.season import SeasonBase, SeasonResponse, SeasonCreate


async def get_seasons(db: Season, user_id: UUID) -> List[SeasonResponse]:
    try:
        items = db.query(Season).filter(Season.user_id == user_id).all()
        seasons = [SeasonResponse.from_orm(item) for item in items]
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='No seasons found')
    return seasons


async def create_season(db: Session, season: SeasonBase) -> SeasonCreate:
    try:
        db_season = Season(**season.dict(), uuid=uuid4())
        db.add(db_season)
        db.commit()
        db.refresh(db_season)
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Season not created')
    return SeasonCreate.from_orm(db_season)


async def delete_seasons(db: Session, user_id: UUID, season_id: UUID) -> SeasonResponse:
    try:
        db_season = db.query(Season).filter(Season.user_id == user_id,
                                            Season.uuid == season_id).first()
        db.delete(db_season)
        db.commit()
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Season not deleted')
    return SeasonResponse.from_orm(db_season)


async def update_season(db: Session,
                        user_id: UUID,
                        season_id: UUID,
                        season: SeasonCreate) -> SeasonResponse:
    try:
        db_season = db.query(Season).filter(Season.user_id == user_id,
                                            Season.uuid == season_id).first()
        db_season.name = season.name
        db_season.game_format = season.game_format
        db_season.start_date = season.start_date
        db_season.end_date = season.end_date
        db.commit()
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Season not updated')
    return SeasonResponse.from_orm(db_season)
