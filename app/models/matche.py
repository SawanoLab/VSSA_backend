from database import Base
from sqlalchemy import Column, ForeignKey, DATETIME, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Matche(Base, TimestampMixin):
    __tablename__ = 'matches'
    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    start_day = Column(DATETIME, nullable=False)
    created_at = Column(DATETIME, nullable=False)
    # UUID (foreignKey links to Teams table's UUID)
    home_team_id = Column(UUIDType(binary=False),
                          ForeignKey('teams.uuid'),
                          nullable=False)
    # UUID (foreignKey links to Teams table's UUID)
    away_team_id = Column(UUIDType(binary=False),
                          ForeignKey('teams.uuid'),
                          nullable=False)
    home_score = Column(Integer, nullable=False)
    away_score = Column(Integer, nullable=False)
    user_id = Column(UUIDType(binary=False),
                     ForeignKey('users.uuid'),
                     nullable=False)

    user = relationship(
        'User',
        back_populates='matches'
    )

    home_team = relationship(
        'Team',
        foreign_keys=[home_team_id],
        back_populates='matches_home'
    )

    away_team = relationship(
        'Team',
        foreign_keys=[away_team_id],
        back_populates='matches_away'
    )

