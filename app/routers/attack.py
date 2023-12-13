from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.attack import AttackGet, AttackBase
from database import get_db
from typing import List
import cruds.attack as crud_attack


attack_router = APIRouter()


@attack_router.get('/', response_model=List[AttackGet])
async def get_attacks(user_id: str,
                      match_id: str,
                      db: Session = Depends(get_db)):
    items = await crud_attack.get_attacks(db, user_id, match_id)
    return items


@attack_router.post('/', response_model=AttackBase)
async def create_attack(attack: AttackBase,
                        db: Session = Depends(get_db)):
    item = await crud_attack.create_attack(db, attack)
    return item


@attack_router.delete('/{attack_id}', response_model=AttackBase)
async def delete_attack(user_id: str, attack_id: str, db: Session = Depends(get_db)):
    item = await crud_attack.delete_attack(db, user_id, attack_id)
    return item
