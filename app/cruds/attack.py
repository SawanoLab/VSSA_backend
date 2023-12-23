from uuid import uuid4
from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from models.attack import Attack
from schemas.attack import AttackBase, AttackResponse
from utils.logger import get_logger


async def get_attacks(db: Session,
                      user_id: str,
                      match_id: str) -> List[AttackResponse]:
    try:
        items = db.query(Attack).filter(Attack.user_id == user_id,
                                        Attack.match_id == match_id).all()
        attacks = [AttackResponse.from_orm(item) for item in items]
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='No attacks found')
    return attacks


async def create_attack(db: Session,
                        attack: AttackBase) -> AttackResponse:
    try:
        db_attack = Attack(**attack.dict(), uuid=uuid4())
        db.add(db_attack)
        db.commit()
        db.refresh(db_attack)
    except Exception:
        get_logger().error('Attack not created')
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Attack not created')
    return AttackResponse.from_orm(db_attack)


async def delete_attack(db: Session,
                        user_id: str,
                        attack_id: str) -> AttackResponse:
    try:
        db_attack = db.query(Attack).filter(Attack.user_id == user_id,
                                            Attack.uuid == attack_id).first()
        db.delete(db_attack)
        db.commit()
    except Exception:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Attack not deleted')
    return AttackResponse.from_orm(db_attack)
