from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.team import TeamBase, TeamGet
from database import get_db
from typing import List
import cruds.team as crud_team


team_router = APIRouter()


@team_router.get('/', response_model=List[TeamGet])
async def get_teams(user_id: str, db: Session = Depends(get_db)):
    items = crud_team.get_teams(db, user_id)
    return items


@team_router.post('/', response_model=TeamBase)
async def create_team(team: TeamBase, db: Session = Depends(get_db)):
    db_team = crud_team.create_team(db, team)
    return db_team
