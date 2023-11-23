from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.match import MatchRequest, MatchPostRequest
import cruds.match as crud_match
from database import get_db


match_router = APIRouter()


@match_router.get('/', response_model=MatchRequest)
async def get_matches(match_id: str, db: Session = Depends(get_db)):
    item = crud_match.get_match(db=db, match_id=match_id)
    return item


@match_router.post('/', response_model=MatchPostRequest)
async def create_match(match: MatchPostRequest, db: Session = Depends(get_db)):
    item = crud_match.create_match(db=db, match=match)
    return item
