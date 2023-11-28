from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.match import MatchRequest, MatchPostRequest
import cruds.match as crud_match
from database import get_db


match_router = APIRouter()


@match_router.get('/', response_model=List[MatchRequest])
async def get_matches(user_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud_match.get_matches(db=db,
                                   user_id=user_id,
                                   skip=skip,
                                   limit=limit)
    return items


@match_router.get('/{match_id}', response_model=MatchRequest)
async def get_match(user_id: str, match_id: str, db: Session = Depends(get_db)):
    item = crud_match.get_match(db=db, user_id=user_id, match_id=match_id)
    return item


@match_router.post('/', response_model=MatchPostRequest)
async def create_match(match: MatchPostRequest, db: Session = Depends(get_db)):
    item = crud_match.create_match(db=db,
                                   matchPostRequest=match)
    return item
