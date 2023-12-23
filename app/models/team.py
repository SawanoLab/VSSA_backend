from database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from .mixins import TimestampMixin


class Teams(Base, TimestampMixin):
    __tablename__ = 'teams'
    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uuid4)
    name = Column(String(128), nullable=False)
    code = Column(String(128), nullable=False)
    director = Column(String(128), nullable=True)
    coach = Column(String(128), nullable=True)
    trainer = Column(String(128), nullable=True)
    doctor = Column(String(128), nullable=True)
    season_id = Column(UUIDType(binary=False),
                       ForeignKey('seasons.uuid'),
                       nullable=False)
    user_id = Column(UUIDType(binary=False),
                     ForeignKey('users.uuid'),
                     nullable=False)

    user = relationship(
        'User',
        back_populates='teams'
    )

    season = relationship(
        'Season',
        back_populates='teams'
    )

    players = relationship(
        'Player',
        back_populates='team'
    )

    home_matches = relationship(
        'Match',
        foreign_keys='Match.home_team_id',
        back_populates='home_team'
    )

    away_matches = relationship(
        'Match',
        foreign_keys='Match.away_team_id',
        back_populates='away_team'
    )

    attacks = relationship(
        'Attack',
        back_populates='team'
    )

    matchscore = relationship(
        'MatchScore',
        back_populates='score_team'
    )
