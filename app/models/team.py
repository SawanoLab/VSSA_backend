from database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Team(Base, TimestampMixin):
    __tablename__ = 'teams'
    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    team_abbreviation = Column(String(128), nullable=False)
    team_name = Column(String(128), nullable=False)
    director_name = Column(String(128), nullable=False)

    matches_home = relationship(
        'Matche',
        foreign_keys='Matche.home_team_id',
        back_populates='home_team'
    )

    matches_away = relationship(
        'Matche',
        foreign_keys='Matche.away_team_id',
        back_populates='away_team'
    )

    teams_players = relationship(
        'TeamsPlayer',
        back_populates='team'
    )
