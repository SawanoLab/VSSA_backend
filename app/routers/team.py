from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.team import TeamBase, TeamResponse
from database import get_db
from typing import List
import cruds.team as crud_team


team_router = APIRouter()


@team_router.get('/', response_model=List[TeamResponse])
async def get_teams(user_id: str, db: Session = Depends(get_db)):
    items = await crud_team.get_teams(db, user_id)
    return items


@team_router.post('/', response_model=TeamResponse)
async def create_team(team: TeamBase, db: Session = Depends(get_db)):
    db_team = await crud_team.create_team(db, team)
    return db_team


@team_router.delete('/{team_id}', response_model=TeamResponse)
async def delete_team(user_id: str, team_id: str, db: Session = Depends(get_db)):
    db_team = await crud_team.delete_team(db, user_id, team_id)
    return db_team


@team_router.put('/{team_id}', response_model=TeamResponse)
async def update_team(team: TeamBase,
                      team_id: str,
                      db: Session = Depends(get_db)):
    db_team = await crud_team.update_team(db, team, team_id)
    return db_team
