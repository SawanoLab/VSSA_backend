from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.season import Season
from schemas.season import SeasonBase, SeasonGet
from uuid import uuid4
from typing import List
from starlette.status import HTTP_404_NOT_FOUND
from uuid import UUID


def get_seasons(db: Season, user_id: UUID) -> List[SeasonGet]:
    try:
        items = db.query(Season).filter(Season.user_id == user_id).all()
        seasons = [SeasonGet.from_orm(item) for item in items]
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='No seasons found')
    return seasons


def create_season(db: Session, season: SeasonBase) -> SeasonBase:
    try:
        db_season = Season(**season.dict(), uuid=uuid4())
        db.add(db_season)
        db.commit()
        db.refresh(db_season)
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Season not created')
    return SeasonBase.from_orm(db_season)
