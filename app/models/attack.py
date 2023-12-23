from database import Base
from sqlalchemy import Column, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin
from enums.attack import AttackBallType, AttackSkill, AttackEvaluationType


class Attack(Base, TimestampMixin):
    __tablename__ = 'attacks'
    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid4)

    home_team_score = Column(Integer, nullable=False, default=0)
    home_team_set_score = Column(Integer, nullable=False, default=0)

    away_team_score = Column(Integer, nullable=False, default=0)
    away_team_set_score = Column(Integer, nullable=False, default=0)

    attack_start_zone = Column(Integer, nullable=False)
    attack_end_zone = Column(Integer, nullable=False)

    attack_ball_type = Column(Enum(AttackBallType), nullable=False)
    attack_skill = Column(Enum(AttackSkill), nullable=False)
    attack_evaluation = Column(Enum(AttackEvaluationType), nullable=False)

    user_id = Column(UUIDType(binary=False),
                     ForeignKey('users.uuid'), nullable=False)
    match_id = Column(UUIDType(binary=False), ForeignKey(
        'matchs.uuid'), nullable=False)
    team_id = Column(UUIDType(binary=False),
                     ForeignKey('teams.uuid'), nullable=False)
    player_id = Column(UUIDType(binary=False), ForeignKey(
        'players.uuid'), nullable=False)

    user = relationship('User', back_populates='attacks')
    match = relationship('Match', back_populates='attacks')
    team = relationship('Teams', back_populates='attacks')
    player = relationship('Player', back_populates='attacks')
