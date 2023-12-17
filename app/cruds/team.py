from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
from typing import List
from uuid import UUID, uuid4
from models.team import Teams
from schemas.team import TeamBase, TeamGet


async def get_teams(db: Session, user_id: UUID) -> List[TeamGet]:
    try:
        items = db.query(Teams).filter(Teams.user_id == user_id).all()
        teams = [TeamGet.from_orm(item) for item in items]
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='No teams found')
    return teams


async def create_team(db: Session, team: TeamBase) -> TeamBase:
    try:
        db_team = Teams(**team.dict(),
                        uuid=uuid4())
        db.add(db_team)
        db.commit()
        db.refresh(db_team)
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Could not create team')
    return TeamBase.from_orm(db_team)
